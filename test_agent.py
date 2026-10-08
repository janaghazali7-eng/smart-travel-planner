from agent import create_trip_plan


print("=" * 60)
print("Testing Smart Travel Planner Agent")
print("=" * 60)


result = create_trip_plan(
    destination="Riyadh",
    days=2,
    travelers=2,
    budget="متوسطة",
    interests="الأماكن السياحية والتسوق والقهوة",
    food="مطاعم عربية",
    transport="DRIVE"
)


print("\n")
print("=" * 60)
print("TRIP PLAN")
print("=" * 60)
print(result)