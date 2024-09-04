import os

def replace_dir_with_element_in_frontmatter():
    # Get the current working directory (where the .py file and markdown files are located)
    directory = os.getcwd()

    # Iterate through all markdown files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            
            # Read the content of the markdown file
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Modify the content by replacing 'DIR:' with 'ELEMENT:' within the frontmatter
            in_frontmatter = False
            updated_content = []
            for line in content:
                if line.strip() == "---":  # Detect YAML frontmatter start/end
                    in_frontmatter = not in_frontmatter
                
                if in_frontmatter and line.startswith("DIR:"):
                    line = line.replace("DIR:", "ELEMENT:")  # Replace DIR: with ELEMENT:

                updated_content.append(line)
            
            # Write the updated content back to the markdown file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(updated_content)

# Call the function to update the files in the current directory
replace_dir_with_element_in_frontmatter()

print("Replacement completed.")
