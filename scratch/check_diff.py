import json
import re

def extract_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract the 'data = { ... }' part using regex or eval (carefully)
    match = re.search(r'data = (\{.*?\})\n\nwith open', content, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return None

data1 = extract_data('generate_json.py')
data2 = extract_data('update_json.py')

def get_uni_names(data):
    names = set()
    for city in data['cities']:
        for uni in city['universities']:
            names.add(uni['name'])
    return names

names1 = get_uni_names(data1)
names2 = get_uni_names(data2)

only_in_1 = names1 - names2
only_in_2 = names2 - names1

print(f"Only in generate_json.py: {only_in_1}")
print(f"Only in update_json.py: {len(only_in_2)} items")
