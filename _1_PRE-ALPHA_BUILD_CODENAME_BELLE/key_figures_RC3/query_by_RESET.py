import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Base directory containing the subdirectories with Markdown files
base_directory = script_directory
# Directory where all the Markdown files will be dumped
target_directory = script_directory

# Walk through the base directory recursively
for root, subdirs, files in os.walk(base_directory):
    if root == target_directory:
        continue  # Skip the target directory
    
    for filename in files:
        if filename.endswith(".md"):
            file_path = os.path.join(root, filename)
            
            # Handle filename conflicts
            target_path = os.path.join(target_directory, filename)
            if os.path.exists(target_path):
                base, ext = os.path.splitext(filename)
                # Append the folder name from where the file is coming to avoid conflicts
                target_path = os.path.join(target_directory, f"{base}_{os.path.basename(root)}{ext}")
            
            # Move the file to the target directory
            shutil.move(file_path, target_path)
            print(f'Moved: {filename} from {root} to {target_directory}')

# After moving all files, clean up empty subdirectories
for root, subdirs, files in os.walk(base_directory, topdown=False):
    # Skip the target directory
    if root == target_directory:
        continue
    
    # Remove subdirectories if they are empty
    if not os.listdir(root):
        os.rmdir(root)
        print(f'Deleted empty directory: {root}')
