import json
import os
import time
import requests
import re

JSON_FILE = "metro_manila_universities.json"
USER_AGENT = "UniversityHunt_Data_Enrichment_Project"

print("🚀 Starting SUPER-SEARCH Coordinate Research...")

def clean_name_for_api(name):
    """Removes abbreviations in parentheses and common suffixes to help the API."""
    # 1. Remove everything inside parentheses: "UP Manila (UPM)" -> "UP Manila"
    name = re.sub(r'\(.*?\)', '', name)
    # 2. Remove suffixes like " - Manila" or " - Main"
    name = re.sub(r'\s*-\s*.*$', '', name)
    # 3. Remove trailing spaces
    return name.strip()

def get_coordinates(university_name, city):
    # Try Variation 1: Cleaned Name + City
    cleaned_name = clean_name_for_api(university_name)
    queries = [
        f"{cleaned_name}, {city}, Metro Manila, Philippines",
        f"{cleaned_name}, Metro Manila, Philippines",
        f"{university_name}, Philippines"
    ]
    
    headers = {'User-Agent': USER_AGENT}
    
    for query in queries:
        url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=1"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return float(data[0]['lat']), float(data[0]['lon'])
        except Exception:
            pass
        time.sleep(0.2) # Short pause between variations
    
    return None, None

def main():
    if not os.path.exists(JSON_FILE):
        print(f"❌ Error: Could not find {JSON_FILE}")
        return

    with open(JSON_FILE, "r", encoding='utf-8') as f:
        data = json.load(f)

    total_schools = sum(len(city["universities"]) for city in data["cities"])
    count = 0

    for city in data["cities"]:
        city_name = city["name"]
        print(f"\n📍 Processing city: {city_name}")
        
        for uni in city["universities"]:
            count += 1
            if "lat" not in uni or "lng" not in uni:
                print(f"  [{count}/{total_schools}] Hunting: {uni['name']}...", end=" ")
                lat, lng = get_coordinates(uni["name"], city_name)
                
                if lat and lng:
                    uni["lat"] = lat
                    uni["lng"] = lng
                    print("✅ FOUND!")
                else:
                    print("❌ Still Not Found.")
                
                time.sleep(1) # Respect API limit
            else:
                print(f"  [{count}/{total_schools}] {uni['name']} already has coords. Skipping.")

    with open(JSON_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("\n✨ ALL DONE: Coordinates updated using Super-Search.")

if __name__ == "__main__":
    main()