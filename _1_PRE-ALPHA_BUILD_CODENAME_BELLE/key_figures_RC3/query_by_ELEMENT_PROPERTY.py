import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter valid categories (ELEMENT)
valid_elements = ["STRUCTURE", "PERSPECTIVES", "RHETORIC", "CHARACTER", "SPACE", "TIME"]

# Valid PROPERTY values
valid_properties = ["FABULA", "SYUZHET", "FUNCTION"]

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

        # Debug print
        print(f'Processing file: {filename}')
        print(f'YAML data: {yaml_data}')
        
        if yaml_data:
            # Extract ELEMENT and PROPERTY from YAML frontmatter
            element_value = yaml_data.get('ELEMENT', '').strip().upper()
            property_value = yaml_data.get('PROPERTY', '').strip().upper()

            # Validate ELEMENT and PROPERTY values
            if element_value in valid_elements:
                if property_value in valid_properties:
                    output_directory = os.path.join(base_output_directory, element_value, property_value)
                else:
                    output_directory = os.path.join(base_output_directory, element_value)
            else:
                print(f'Unrecognized ELEMENT in file: {filename}')
                continue

            # Create the output directory if it does not exist
            os.makedirs(output_directory, exist_ok=True)

            # Move the file to the appropriate output directory
            try:
                shutil.move(filepath, os.path.join(output_directory, filename))
                print(f'Moved: {filename} to {output_directory}')
            except Exception as e:
                print(f"Error moving file {filename}: {e}")
        else:
            print(f'No valid YAML data in file: {filename}')
