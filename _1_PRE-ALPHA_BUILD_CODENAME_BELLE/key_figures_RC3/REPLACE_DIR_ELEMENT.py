import os
import yaml
import re

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1), match.start(), match.end()
    return None, None, None

# Function to replace DIR with ELEMENT and reorder YAML fields
def replace_and_reorder_yaml(yaml_content):
    try:
        yaml_data = yaml.safe_load(yaml_content)
        
        # Ensure 'ELEMENT' is added after 'Prima-Forma'
        element_value = yaml_data.get('ELEMENT', None)
        
        # Reorder the fields explicitly
        ordered_yaml = {}
        # UID should always come first
        if 'UID' in yaml_data:
            ordered_yaml['UID'] = yaml_data.pop('UID')
        # Title should come second
        if 'Title' in yaml_data:
            ordered_yaml['Title'] = yaml_data.pop('Title')
        
        # Add all other fields except Prima-Forma and ELEMENT
        for key, value in list(yaml_data.items()):
            if key != 'Prima-Forma' and key != 'ELEMENT':
                ordered_yaml[key] = yaml_data.pop(key)

        # Prima-Forma should be followed by ELEMENT
        if 'Prima-Forma' in yaml_data:
            ordered_yaml['Prima-Forma'] = yaml_data.pop('Prima-Forma')
            if element_value:
                ordered_yaml['ELEMENT'] = element_value

        # Add any remaining fields
        for key, value in yaml_data.items():
            ordered_yaml[key] = value

        return yaml.dump(ordered_yaml, default_flow_style=False)
    except yaml.YAMLError as e:
        print(f"YAML error: {e}")
    return yaml_content

# Iterate over each file in the directory
for filename in os.listdir(script_directory):
    if filename.endswith(".md"):
        filepath = os.path.join(script_directory, filename)

        # Read the file content
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            continue

        # Extract the YAML frontmatter
        yaml_content, yaml_start, yaml_end = extract_yaml_frontmatter(content)
        
        if yaml_content:
            # Replace DIR with ELEMENT and reorder the fields
            updated_yaml_content = replace_and_reorder_yaml(yaml_content)
            
            # Update the file content
            updated_content = content[:yaml_start] + "---\n" + updated_yaml_content + "---\n" + content[yaml_end:]
            
            # Write the updated content back to the file
            try:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f'Updated: {filename}')
            except Exception as e:
                print(f"Error writing file {filename}: {e}")

print("Replacement and reordering completed.")
