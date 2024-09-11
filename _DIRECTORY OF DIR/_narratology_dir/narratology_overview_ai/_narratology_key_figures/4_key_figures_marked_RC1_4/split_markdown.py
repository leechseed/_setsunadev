import os

# Define the input Markdown file
input_file = r'C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_narratology_dir\narratology_overview_ai\_narratology_key_figures\_key_figures_marked_split_3\17_Ryan_split\17.3_Ryan_marked.md'

# Get the directory of the input file
output_dir = os.path.dirname(input_file)

# Read the entire file
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content based on the delimiter (***)
sections = content.split('***')

# Save each section to a new file in the same directory as the input file
for i, section in enumerate(sections):
    # Define the filename for each section
    filename = os.path.join(output_dir, f'section_{i + 1}.md')

    # Write the section to a new file
    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.write(section.strip())  # Use .strip() to remove any leading/trailing whitespace

    print(f'Section {i + 1} saved as {filename}')
