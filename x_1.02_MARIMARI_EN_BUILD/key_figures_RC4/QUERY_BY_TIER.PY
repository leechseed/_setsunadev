import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter category is TIER with possible values
query_tier_values = [
    "Tier 1",
    "Tier 2",
    "Tier 3",
    "Tier 4",
    "Tier 5",
    "Tier 6"
]

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
        
        if yaml_data and 'TIER' in yaml_data:
            # Normalize and check if the value in 'TIER' is one of the specified categories
            tier_value = yaml_data['TIER'].strip()
            if tier_value in query_tier_values:
                # Extract the tier number for folder naming (e.g., "Tier 1" remains "Tier 1")
                tier_folder = tier_value  # You can modify this if you prefer different folder names

                # Create the output directory based on the TIER value
                output_directory = os.path.join(base_output_directory, tier_folder)
                os.makedirs(output_directory, exist_ok=True)

                # Move the file to the appropriate output directory
                try:
                    shutil.move(filepath, os.path.join(output_directory, filename))
                    print(f'Moved: {filename} to {output_directory}')
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
            else:
                print(f'Unrecognized TIER value in file: {filename}')
        else:
            print(f'No TIER field in file: {filename}')
