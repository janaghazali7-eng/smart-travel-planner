import os
from dotenv import load_dotenv
import requests

load_dotenv()

google_key = os.getenv("GOOGLE_MAPS_API_KEY")

if not google_key:
    print("Google Maps API Key غير موجود ❌")
    exit()

url = "https://routes.googleapis.com/directions/v2:computeRoutes"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": google_key,
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters"
}

data = {
    "origin": {
        "address": "Kingdom Centre Riyadh"
    },
    "destination": {
        "address": "Riyadh Park"
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE",
    "computeAlternativeRoutes": False,
    "units": "METRIC"
}

response = requests.post(
    url,
    headers=headers,
    json=data,
    timeout=20
)

print("Status Code:", response.status_code)

if response.ok:
    result = response.json()
    routes = result.get("routes", [])

    if routes:
        route = routes[0]

        distance = route.get("distanceMeters", 0) / 1000
        duration = route.get("duration", "غير متوفر")

        print("\nGoogle Routes يعمل ✅")
        print(f"المسافة: {distance:.2f} كم")
        print(f"المدة: {duration}")
    else:
        print("لم يتم العثور على مسار ❌")

else:
    print("Google Routes فيه مشكلة ❌")
    print(response.text)