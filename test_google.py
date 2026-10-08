import os
from dotenv import load_dotenv
import requests

load_dotenv()

google_key = os.getenv("GOOGLE_MAPS_API_KEY")

if not google_key:
    print("Google Maps API Key غير موجود ❌")
    exit()

url = "https://places.googleapis.com/v1/places:searchText"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": google_key,
    "X-Goog-FieldMask": (
        "places.displayName,"
        "places.formattedAddress,"
        "places.rating,"
        "places.userRatingCount,"
        "places.googleMapsUri"
    )
}

data = {
    "textQuery": "tourist attractions in Riyadh",
    "languageCode": "ar",
    "pageSize": 5
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

    print("\nGoogle Places يعمل ✅\n")

    for place in result.get("places", []):
        name = place.get("displayName", {}).get(
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

        print(f"📍 {name}")
        print(f"العنوان: {address}")
        print(f"التقييم: {rating}")
        print("-" * 40)

else:
    print("Google Places فيه مشكلة ❌")
    print(response.text)