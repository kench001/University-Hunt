import json
import os

data = {
    "cities": []
}

def add_university(city_name, uni_name, type, info, programs, tuition):
    city = next((c for c in data["cities"] if c["name"] == city_name), None)
    if not city:
        city = {"name": city_name, "universities": []}
        data["cities"].append(city)
    
    city["universities"].append({
        "name": uni_name,
        "type": type,
        "info": info,
        "programs": programs,
        "tuition": tuition
    })

def save_data():
    with open("universities_data.json", "w") as f:
        json.dump(data, f, indent=2)

# I will call this script later to update the JSON
