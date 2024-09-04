import os
import re

def replace_dir_with_element_in_frontmatter():
    # Get the current working directory
    directory = os.getcwd()

    # Regular expression to match the YAML frontmatter block
    yaml_pattern = re.compile(r'^---[\s\S]*?---', re.MULTILINE)
    # Pattern to find DIR: within the YAML frontmatter
    dir_pattern = re.compile(r'^DIR:.*$', re.MULTILINE)

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            
            # Read the content of the file
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # Find the YAML frontmatter block
            yaml_match = yaml_pattern.search(content)
            if yaml_match:
                frontmatter = yaml_match.group(0)
                
                # Replace 'DIR:' with 'ELEMENT:' in the YAML frontmatter
                updated_frontmatter = dir_pattern.sub(lambda m: m.group().replace('DIR:', 'ELEMENT:'), frontmatter)
                
                # Replace the old YAML frontmatter with the updated one in the content
                updated_content = content.replace(frontmatter, updated_frontmatter)
                
                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(updated_content)

# Call the function to update the files in the current directory
replace_dir_with_element_in_frontmatter()

print("Replacement completed.")
