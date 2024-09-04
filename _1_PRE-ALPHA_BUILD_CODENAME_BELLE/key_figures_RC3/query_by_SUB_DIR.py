import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter category and subcategories
query_categories = {
    "STRUCTURE": ["ARCHITECTURE", "DESIGN"],
    "PERSPECTIVES": ["VIEWPOINTS", "ANGLES"],
    "SEMANTICS": ["MEANING", "INTERPRETATION"],
    "CHARACTER": ["PERSONALITY", "TRAITS"],
    "SPACE": ["DIMENSION", "LOCATION"],
    "TIME": ["HISTORICAL", "TEMPORAL"]
}

# Special case handling for STRUCTURE and CAT
special_structure_subcategories = ["FABULA", "SZU"]

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"YAML error: {e}")
    return None

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        filepath = os.path.join(input_directory, filename)

        # Read the file content
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            continue

        # Extract the YAML frontmatter
        yaml_data = extract_yaml_frontmatter(content)
        
        if yaml_data and 'DIR' in yaml_data:
            # Extract category and subcategory
            dir_data = yaml_data['DIR']
            category = dir_data.get('category', '').strip().upper()
            subcategory = dir_data.get('subcategory', '').strip().upper()

            # Handle special case for STRUCTURE and CAT
            if category == "STRUCTURE" and 'CAT' in dir_data:
                cat_value = dir_data.get('CAT', '').strip().upper()
                if cat_value in special_structure_subcategories:
                    output_directory = os.path.join(base_output_directory, category, cat_value)
                    os.makedirs(output_directory, exist_ok=True)
                else:
                    output_directory = os.path.join(base_output_directory, category)
            else:
                # Handle general categories and subcategories
                if category in query_categories:
                    if subcategory in query_categories[category]:
                        output_directory = os.path.join(base_output_directory, category, subcategory)
                        os.makedirs(output_directory, exist_ok=True)
                    else:
                        print(f'Unrecognized subcategory in file: {filename}')
                        continue
                else:
                    print(f'Unrecognized category in file: {filename}')
                    continue

            # Move the file to the appropriate output directory
            try:
                shutil.move(filepath, os.path.join(output_directory, filename))
                print(f'Moved: {filename} to {output_directory}')
            except Exception as e:
                print(f"Error moving file {filename}: {e}")
        else:
            print(f'No DIR field in file: {filename}')
