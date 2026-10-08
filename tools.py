import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool


# تحميل مفاتيح API من .env
load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


# =========================================================
# Google Places Tool
# =========================================================

@tool
def search_places(
    destination: str,
    place_type: str = "tourist attractions"
) -> str:
    """
    البحث عن أماكن في الوجهة باستخدام Google Places API.
    يمكن البحث عن أماكن سياحية أو مطاعم أو مقاهي.
    """

    if not GOOGLE_MAPS_API_KEY:
        return "Google Maps API Key غير موجود."

    url = "https://places.googleapis.com/v1/places:searchText"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": (
            "places.displayName,"
            "places.formattedAddress,"
            "places.rating,"
            "places.userRatingCount,"
            "places.googleMapsUri"
        )
    }

    data = {
        "textQuery": f"{place_type} in {destination}",
        "languageCode": "ar",
        "pageSize": 8
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=20
        )

        response.raise_for_status()

        result = response.json()

        places = result.get("places", [])

        if not places:
            return f"لم يتم العثور على {place_type} في {destination}."

        results = []

        for place in places:

            name = place.get(
                "displayName",
                {}
            ).get(
                "text",
                "غير معروف"
            )

            address = place.get(
                "formattedAddress",
                "العنوان غير متوفر"
            )

            rating = place.get(
                "rating",
                "لا يوجد"
            )

            reviews = place.get(
                "userRatingCount",
                0
            )

            maps_url = place.get(
                "googleMapsUri",
                ""
            )

            results.append(
                f"""
الاسم: {name}
العنوان: {address}
التقييم: {rating}
عدد التقييمات: {reviews}
Google Maps: {maps_url}
"""
            )

        return "\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"حدث خطأ في Google Places API: {e}"

    except Exception as e:
        return f"حدث خطأ غير متوقع: {e}"


# =========================================================
# Google Routes Tool
# =========================================================

@tool
def calculate_route(
    origin: str,
    destination: str,
    transport: str = "DRIVE"
) -> str:
    """
    حساب المسافة والمدة بين موقعين باستخدام Google Routes API.
    """

    if not GOOGLE_MAPS_API_KEY:
        return "Google Maps API Key غير موجود."

    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": (
            "routes.duration,"
            "routes.distanceMeters"
        )
    }

    transport = transport.upper()

    if transport in ["WALK", "WALKING"]:
        travel_mode = "WALK"
    else:
        travel_mode = "DRIVE"

    data = {
        "origin": {
            "address": origin
        },
        "destination": {
            "address": destination
        },
        "travelMode": travel_mode,
        "computeAlternativeRoutes": False,
        "units": "METRIC"
    }

    if travel_mode == "DRIVE":
        data["routingPreference"] = "TRAFFIC_AWARE"

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=20
        )

        response.raise_for_status()

        result = response.json()

        routes = result.get("routes", [])

        if not routes:
            return "لم يتم العثور على مسار."

        route = routes[0]

        distance_meters = route.get(
            "distanceMeters",
            0
        )

        distance_km = distance_meters / 1000

        duration = route.get(
            "duration",
            "غير متوفر"
        )

        return (
            f"المسافة: {distance_km:.2f} كم\n"
            f"المدة التقريبية: {duration}\n"
            f"وسيلة النقل: {travel_mode}"
        )

    except requests.exceptions.RequestException as e:
        return f"حدث خطأ في Google Routes API: {e}"

    except Exception as e:
        return f"حدث خطأ غير متوقع: {e}"


# =========================================================
# Restaurant Tool
# =========================================================

@tool
def search_restaurants(destination: str) -> str:
    """
    البحث عن المطاعم في الوجهة.
    """

    return search_places.invoke({
        "destination": destination,
        "place_type": "restaurants"
    })


# =========================================================
# Tourist Attractions Tool
# =========================================================

@tool
def search_attractions(destination: str) -> str:
    """
    البحث عن الأماكن السياحية في الوجهة.
    """

    return search_places.invoke({
        "destination": destination,
        "place_type": "tourist attractions"
    })


# =========================================================
# Cafes Tool
# =========================================================

@tool
def search_cafes(destination: str) -> str:
    """
    البحث عن المقاهي في الوجهة.
    """

    return search_places.invoke({
        "destination": destination,
        "place_type": "cafes"
    })