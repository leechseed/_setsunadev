import os
import yaml
import re

# Directory containing the Markdown files
directory = r'C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_narratology_dir\narratology_overview_ai\_narratology_key_figures\4_key_figures_marked_RC1_4\1_Propp_split'

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return None

# Function to sanitize a string for use in filenames
def sanitize_filename_component(component):
    return re.sub(r'[^a-z0-9_]', '', component.lower().replace(' ', '_').replace('/', '_'))

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)

        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extract the YAML frontmatter
        yaml_data = extract_yaml_frontmatter(content)
        
        if yaml_data and 'Author' in yaml_data and 'Title' in yaml_data and 'UID' in yaml_data:
            # Get and sanitize the Author, Title, and UID from the YAML frontmatter
            uid = sanitize_filename_component(yaml_data['UID'].strip())
            title = sanitize_filename_component(yaml_data['Title'].strip())
            author = sanitize_filename_component(yaml_data['Author'].strip())

            # Construct the new filename in the order UID_Title_Author with the .md extension
            new_name = f'{uid}_{title}_{author}.md'

            # Rename the file
            new_filepath = os.path.join(directory, new_name)
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_name}')
