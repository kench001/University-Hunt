import os

def find_research_tool():
    # We search in your user directory for the research.py file
    user_home = os.path.expanduser("~")
    print(f"🔍 Searching for research.py in: {user_home} ...")
    
    found_paths = []
    for root, dirs, files in os.walk(user_home):
        if "research.py" in files:
            # We only want the one inside the antigravity/skills folder
            if "antigravity" in root and "skills" in root:
                full_path = os.path.join(root, "research.py")
                found_paths.append(full_path)

    if found_paths:
        print("\n✅ FOUND IT!")
        for path in found_paths:
            print(f"\nCorrect Path:\n{path}")
        print("\n👉 COPY the path above and paste it into your get_coords.py and debug_coords.py files.")
    else:
        print("\n❌ COULD NOT FIND research.py")
        print("Please check if the antigravity skills are installed correctly.")

if __name__ == "__main__":
    find_research_tool()