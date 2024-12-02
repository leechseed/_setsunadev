import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Function to move UID to the top and Title below UID
def move_uid_and_title(content):
    # Split the content into lines
    lines = content.splitlines()

    uid_line = None
    title_line = None
    author_index = None

    # Find the UID, Title, and Author lines
    for i, line in enumerate(lines):
        if line.startswith("UID:"):
            uid_line = line  # Record UID line
        if line.startswith("Title:"):
            title_line = line  # Record Title line
        if line.startswith("Author:"):
            author_index = i  # Record the position of the Author line

    # Remove UID and Title from their current positions
    lines = [line for line in lines if not line.startswith("UID:") and not line.startswith("Title:")]

    # Reinsert UID at the top (right after '---')
    if uid_line:
        lines.insert(1, uid_line)  # Insert UID as the second line (first is '---')

    # Reinsert Title just above the Author line
    if title_line and author_index is not None:
        lines.insert(author_index, title_line)  # Insert Title just before Author

    # Join the lines back together and return the modified content
    return "\n".join(lines)

# Iterate over each markdown file in the directory
for filename in os.listdir(script_directory):
    if filename.endswith(".md"):
        filepath = os.path.join(script_directory, filename)

        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Process the content to move UID and Title
        updated_content = move_uid_and_title(content)
        
        # Write the updated content back to the markdown file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f'Updated UID and Title position: {filename}')

print("UID moved to the top and Title moved below UID in all markdown files.")
