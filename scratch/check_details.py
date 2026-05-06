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

def get_uni_dict(data):
    unis = {}
    for city in data['cities']:
        for uni in city['universities']:
            unis[uni['name']] = uni
    return unis

unis1 = get_uni_dict(data1)
unis2 = get_uni_dict(data2)

diffs = []
for name, uni in unis1.items():
    if name in unis2:
        if unis1[name] != unis2[name]:
            diffs.append(name)

print(f"Differences in shared universities: {diffs}")
