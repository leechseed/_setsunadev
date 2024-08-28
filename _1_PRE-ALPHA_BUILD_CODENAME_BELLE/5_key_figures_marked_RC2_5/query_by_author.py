import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML query parameters for Author
query_author_values = [
    "Propp", "Genette", "Barthes", "Todorov", "Bal", "Tomashevsky", 
    "Chatman", "Greimas", "Forster", "Rimmon-Kenan", "Brooks", 
    "Booth", "Herman", "Sternberg", "Bakhtin", "Abbott", "Ryan"
]

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return None

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        filepath = os.path.join(input_directory, filename)

        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extract the YAML frontmatter
        yaml_data = extract_yaml_frontmatter(content)
        
        if yaml_data and 'Author' in yaml_data:
            if yaml_data['Author'] in query_author_values:
                # Create the output directory based on the Author query parameter
                output_directory = os.path.join(base_output_directory, yaml_data['Author'])
                os.makedirs(output_directory, exist_ok=True)

                # Move the file to the appropriate output directory
                shutil.move(filepath, os.path.join(output_directory, filename))
                print(f'Moved: {filename} to {output_directory}')
