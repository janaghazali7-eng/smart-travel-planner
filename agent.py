import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

from prompt import travel_prompt
from database import save_trip

from tools import (
    search_places,
    search_restaurants,
    search_attractions,
    search_cafes,
    calculate_route
)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY غير موجود. تأكد من إضافته في ملف .env"
    )

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=GROQ_API_KEY
)

tools = [
    search_places,
    search_restaurants,
    search_attractions,
    search_cafes,
    calculate_route
]

agent = create_tool_calling_agent(
    llm,
    tools,
    travel_prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=15,
    max_execution_time=120
)


def create_trip_plan(
    destination,
    days,
    travelers,
    budget,
    interests,
    food,
    transport
):
    try:
        result = agent_executor.invoke({
            "destination": destination,
            "days": days,
            "travelers": travelers,
            "budget": budget,
            "interests": interests,
            "food": food,
            "transport": transport
        })

        trip_plan = result["output"]

        save_trip(
            destination=destination,
            days=days,
            travelers=travelers,
            budget=budget,
            interests=interests,
            food=food,
            transport=transport,
            trip_plan=trip_plan
        )

        return trip_plan
    except Exception as e:
        return (
            "حدث خطأ أثناء إنشاء خطة الرحلة.\n\n"
            f"تفاصيل الخطأ: {e}"
        )