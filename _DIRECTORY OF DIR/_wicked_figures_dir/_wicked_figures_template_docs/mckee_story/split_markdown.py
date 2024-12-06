import os
import re

def split_markdown_file(input_file_path, delimiter='---', output_prefix='section_'):
    """
    Splits a Markdown file into separate files based on a specified delimiter.

    Args:
        input_file_path (str): The full path to the input Markdown file.
        delimiter (str): The delimiter string to split the document. Default is '---'.
        output_prefix (str): The prefix for the output files. Default is 'section_'.

    Returns:
        None
    """
    # Ensure the input file exists
    if not os.path.isfile(input_file_path):
        print(f"Error: The file {input_file_path} does not exist.")
        return

    # Get the directory of the input file
    output_dir = os.path.dirname(input_file_path)

    # Read the entire file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define a regex pattern to split on delimiter surrounded by optional whitespace and newlines
    # This accounts for delimiters that are on their own lines
    pattern = rf'\n\s*{re.escape(delimiter)}\s*\n'

    # Split the content based on the delimiter pattern
    sections = re.split(pattern, content)

    # Remove any empty sections resulting from the split
    sections = [section.strip() for section in sections if section.strip()]

    # Check if any sections were found
    if not sections:
        print("No sections found to split.")
        return

    # Save each section to a new file in the same directory as the input file
    for i, section in enumerate(sections, start=1):
        # Optionally, extract a title from the section to use in the filename
        # Here, we'll use the first heading in the section if available
        title_match = re.search(r'^#\s+(.*)', section, re.MULTILINE)
        if title_match:
            # Clean the title to create a valid filename
            title = title_match.group(1).strip().replace(' ', '_').replace('/', '_')
            filename = os.path.join(output_dir, f"{output_prefix}{i}_{title}.md")
        else:
            # Fallback to numbered filenames if no title is found
            filename = os.path.join(output_dir, f"{output_prefix}{i}.md")

        try:
            # Write the section to a new file
            with open(filename, 'w', encoding='utf-8') as output_file:
                output_file.write(section + '\n')  # Add a newline at the end for consistency

            print(f"Section {i} saved as {filename}")
        except Exception as e:
            print(f"Failed to write section {i} to {filename}: {e}")

if __name__ == "__main__":
    # Define the input Markdown file
    input_file = r'C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_DIRECTORY OF DIR\_wicked_figures_dir\_wicked_figures_template_docs\mckee_story\mckee_story_5.md'
    
    # Call the function to split the Markdown file
    split_markdown_file(input_file)
