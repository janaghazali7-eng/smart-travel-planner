from tools import (
    search_restaurants,
    search_attractions,
    search_cafes,
    calculate_route
)


print("=" * 50)
print("Testing LangChain Tools")
print("=" * 50)


# اختبار المطاعم
print("\n🍽️ Restaurants:")
result = search_restaurants.invoke({
    "destination": "Riyadh"
})
print(result)


# اختبار الأماكن السياحية
print("\n🏛️ Tourist Attractions:")
result = search_attractions.invoke({
    "destination": "Riyadh"
})
print(result)


# اختبار المقاهي
print("\n☕ Cafes:")
result = search_cafes.invoke({
    "destination": "Riyadh"
})
print(result)


# اختبار المسارات
print("\n🚗 Route:")
result = calculate_route.invoke({
    "origin": "Kingdom Centre Riyadh",
    "destination": "Riyadh Park",
    "transport": "DRIVE"
})
print(result)