import json
import re

def extract_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'data = (\{.*?\})\n\nwith open', content, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return None

data1 = extract_data('generate_json.py')
data2 = extract_data('update_json.py')

merged_cities = {}

def merge_data(data):
    for city in data['cities']:
        city_name = city['name']
        if city_name not in merged_cities:
            merged_cities[city_name] = {}
        for uni in city['universities']:
            uni_name = uni['name']
            if uni_name not in merged_cities[city_name]:
                merged_cities[city_name][uni_name] = uni
            else:
                # Merge logic: keep the longer info/tuition
                existing = merged_cities[city_name][uni_name]
                if len(uni['info']) > len(existing['info']):
                    existing['info'] = uni['info']
                if len(uni['tuition']) > len(existing['tuition']):
                    existing['tuition'] = uni['tuition']
                # Merge programs
                existing['programs'] = list(set(existing['programs'] + uni['programs']))

merge_data(data1)
merge_data(data2)

final_data = {"cities": []}
for city_name, unis in merged_cities.items():
    final_data["cities"].append({
        "name": city_name,
        "universities": list(unis.values())
    })

with open('merged_data.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=4)

# Create the final script content
script_template = """import json

data = {data_json}

with open("metro_manila_universities.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON file updated with merged and deduplicated data.")
"""

with open('final_script.py', 'w', encoding='utf-8') as f:
    f.write(script_template.format(data_json=json.dumps(final_data, indent=4, ensure_ascii=False)))
