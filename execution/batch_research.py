import json
import subprocess
import os
import sys

# Constants
JSON_FILE = "metro_manila_universities.json"
SKILL_PATH = r"C:\Users\Justin Loyola\.gemini\antigravity\skills\deep-research\scripts\research.py"
TMP_DIR = ".tmp"
BATCH_SIZE = 10

def load_schools():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    schools = []
    for city in data["cities"]:
        for uni in city["universities"]:
            schools.append({"name": uni["name"], "city": city["name"]})
    return schools

def run_research(batch, batch_id):
    school_list = ", ".join([s["name"] for s in batch])
    query = f"Research the following universities in Metro Manila, Philippines: {school_list}. " \
            f"For each school, find: 1. Rank (local/national), 2. Acceptance Rate, 3. Total Students, " \
            f"4. Official Website, 5. Accurate Tuition (per sem/term), 6. 5-6 Featured/Flagship Programs, " \
            f"7. A 2-3 sentence descriptive info summary."
    
    output_format = "Provide the result as a JSON array of objects. Each object should have keys: " \
                    "name, rank, acceptance_rate, total_students, website, tuition, featured_programs (list), info."
    
    print(f"Running research for Batch {batch_id}...")
    
    cmd = [
        "python", SKILL_PATH,
        "--query", query,
        "--format", output_format,
        "--json"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # The tool might print progress to stdout, so we need to find the JSON part
        output = result.stdout
        # Assuming the tool outputs valid JSON at the end or as the main output
        # Let's save the raw output for now to debug if needed
        os.makedirs(TMP_DIR, exist_ok=True)
        with open(os.path.join(TMP_DIR, f"research_results_{batch_id}.json"), "w") as f:
            f.write(output)
        print(f"Batch {batch_id} completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error in Batch {batch_id}: {e.stderr}")

def main():
    schools = load_schools()
    batches = [schools[i:i + BATCH_SIZE] for i in range(0, len(schools), BATCH_SIZE)]
    
    # For initial testing, run only the first batch
    for i, batch in enumerate(batches[:1]):
        run_research(batch, i + 1)

if __name__ == "__main__":
    main()
