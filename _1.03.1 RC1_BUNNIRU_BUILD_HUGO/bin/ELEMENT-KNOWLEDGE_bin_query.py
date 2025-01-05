import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter category is ELEMENT with possible values
query_element_values = ["STRUCTURE", "PERSPECTIVES", "RHETORIC", "CHARACTER", "SPACE", "TIME"]

# Knowledge type subcategory with possible values
knowledge_type_values = ["TACIT", "EXPLICIT"]

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
        
        if yaml_data and 'ELEMENT' in yaml_data and 'KNOWLEDGE TYPE' in yaml_data:
            # Normalize and check if the value in 'ELEMENT' is one of the specified categories
            element_value = yaml_data['ELEMENT'].strip().upper()
            knowledge_type_value = yaml_data['KNOWLEDGE TYPE'].strip().upper()

            if element_value in [value.upper() for value in query_element_values] and knowledge_type_value in knowledge_type_values:
                # Create the output directory based on the ELEMENT and KNOWLEDGE TYPE values
                output_directory = os.path.join(base_output_directory, element_value, knowledge_type_value)
                os.makedirs(output_directory, exist_ok=True)

                # Move the file to the appropriate output directory
                try:
                    shutil.move(filepath, os.path.join(output_directory, filename))
                    print(f'Moved: {filename} to {output_directory}')
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
            else:
                print(f'Unrecognized ELEMENT or KNOWLEDGE TYPE value in file: {filename}')
        else:
            print(f'No ELEMENT or KNOWLEDGE TYPE field in file: {filename}')
