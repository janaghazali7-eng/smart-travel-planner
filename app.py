import streamlit as st

st.set_page_config(
    page_title="Smart Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, p, label, div {
        text-align: right;
    }

    input, textarea {
        direction: rtl;
        text-align: right;
    }

    [data-baseweb="select"] {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

st.title("✈️ Smart Travel Planner")
st.write("خطط رحلتك بسهولة باستخدام المساعد الذكي")

st.divider()

st.subheader("معلومات الرحلة")

destination = st.text_input(
    "📍 الوجهة",
    placeholder="مثال: Riyadh"
)

days = st.number_input(
    "📅 عدد الأيام",
    min_value=1,
    max_value=30,
    value=2
)

travelers = st.number_input(
    "👥 عدد المسافرين",
    min_value=1,
    max_value=20,
    value=2
)

budget = st.selectbox(
    "💰 الميزانية",
    ["منخفضة", "متوسطة", "مرتفعة"]
)

interests = st.text_input(
    "🎯 الاهتمامات",
    placeholder="مثال: الأماكن السياحية، التسوق، القهوة"
)

food = st.text_input(
    "🍽️ تفضيلات الطعام",
    placeholder="مثال: مطاعم عربية"
)

transport = st.selectbox(
    "🚗 وسيلة التنقل",
    ["DRIVE", "WALK"]
)

st.divider()

if st.button("✨ إنشاء خطة الرحلة", use_container_width=True):

    if not destination:
        st.warning("يرجى إدخال الوجهة أولاً.")

    else:
        st.info("جاري إنشاء خطة الرحلة...")

        from agent import create_trip_plan

        trip_plan = create_trip_plan(
            destination=destination,
            days=days,
            travelers=travelers,
            budget=budget,
            interests=interests,
            food=food,
            transport=transport
        )

        st.success("تم إنشاء خطة الرحلة!")

        st.markdown("## 🗺️ خطة الرحلة")
        st.markdown(trip_plan)