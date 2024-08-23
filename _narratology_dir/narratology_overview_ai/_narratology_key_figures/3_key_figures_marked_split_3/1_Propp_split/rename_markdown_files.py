import os
import yaml
import re

# Directory containing the Markdown files
directory = r'_narratology_dir/narratology_overview_ai/_narratology_key_figures/_key_figures_marked_split_3/1_Propp_split'

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return None

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
            # Get the Author, Title, and UID from the YAML frontmatter
            uid = yaml_data['UID'].strip().lower()
            title = yaml_data['Title'].strip().lower().replace(' ', '_').replace('/', '_')
            author = yaml_data['Author'].strip().lower().replace(' ', '_').replace('/', '_')

            # Construct the new filename in the order UID_Title_Author
            new_name = f'{uid}_{title}_{author}.md'
            new_name = re.sub(r'[^a-z0-9_]', '', new_name)  # Remove non-alphanumeric characters

            # Rename the file
            new_filepath = os.path.join(directory, new_name)
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_name}')
