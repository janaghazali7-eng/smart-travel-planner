from database import create_database, get_saved_trips

create_database()

trips = get_saved_trips()

print("=" * 60)
print("SAVED TRIPS")
print("=" * 60)

for trip in trips:
    print(f"\nTrip ID: {trip[0]}")
    print(f"Destination: {trip[1]}")
    print(f"Days: {trip[2]}")
    print(f"Travelers: {trip[3]}")
    print(f"Budget: {trip[4]}")
    print(f"Interests: {trip[5]}")
    print(f"Food: {trip[6]}")
    print(f"Transport: {trip[7]}")
    print(f"Plan: {trip[8]}")