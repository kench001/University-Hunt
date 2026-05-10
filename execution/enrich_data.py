import json
import re
import os

JSON_FILE = "metro_manila_universities.json"

print("🚀 Starting Data Enrichment...")

CATEGORY_MAP = {
    "Medical": ["Medicine", "Nursing", "Pharmacy", "Physical Therapy", "Dentistry", "Medical Technology"],
    "Engineering & Tech": ["Engineering", "Computer Science", "IT", "Architecture", "Computer Studies"],
    "Business & Law": ["Business", "Accountancy", "Law", "Economics", "Management", "Entrepreneurship"],
    "Arts & Humanities": ["Fine Arts", "Liberal Arts", "Communication", "Psychology", "Music", "Social Sciences"],
    "Education": ["Education", "English", "Mathematics", "Social Sciences"]
}

def extract_numbers(text):
    """Helper to extract all numbers from a string and return them as integers."""
    if not text or not isinstance(text, str):
        return []
    nums = re.findall(r'[\d,]+', text)
    return [int(n.replace(',', '')) for n in nums]

def clean_tuition(tuition_data):
    """Handles both string tuition and dictionary tuition."""
    all_found_nums = []

    # Case 1: Tuition is a Dictionary (e.g., {"Undergraduate": "₱50k", "Graduate": "₱100k"})
    if isinstance(tuition_data, dict):
        for val in tuition_data.values():
            all_found_nums.extend(extract_numbers(val))
    
    # Case 2: Tuition is a String (e.g., "₱50,000 - ₱70,000")
    elif isinstance(tuition_data, str):
        if "Free" in tuition_data and not any(char.isdigit() for char in tuition_data):
            return 0, 0
        all_found_nums.extend(extract_numbers(tuition_data))

    if not all_found_nums:
        return 0, 0
    
    return min(all_found_nums), max(all_found_nums)

def get_category(programs):
    if not isinstance(programs, list):
        return []
    categories = []
    for prog in programs:
        for cat, progs in CATEGORY_MAP.items():
            if any(p.lower() in prog.lower() for p in progs):
                categories.append(cat)
    return list(set(categories))

try:
    if not os.path.exists(JSON_FILE):
        print(f"❌ Error: Could not find {JSON_FILE} in the current directory.")
    else:
        with open(JSON_FILE, "r", encoding='utf-8') as f:
            data = json.load(f)

        for city in data["cities"]:
            for uni in city["universities"]:
                # Handle tuition
                raw_tuition = uni.get("tuition", "")
                t_min, t_max = clean_tuition(raw_tuition)
                uni["tuition_min"] = t_min
                uni["tuition_max"] = t_max
                
                # Handle categories
                uni["categories"] = get_category(uni.get("programs", []))

        with open(JSON_FILE, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print("✅ SUCCESS: Tuition normalized and Categories assigned.")
except Exception as e:
    print(f"❌ CRITICAL ERROR: {e}")