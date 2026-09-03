import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Base directory containing the subdirectories with Markdown files
base_directory = script_directory
# Directory where all the Markdown files will be dumped
target_directory = script_directory

# Iterate over each item in the base directory
for subdir in os.listdir(base_directory):
    subdir_path = os.path.join(base_directory, subdir)
    
    if os.path.isdir(subdir_path) and subdir_path != target_directory:  # Check if it's a directory and not the target directory
        # Iterate over each file in the subdirectory
        for filename in os.listdir(subdir_path):
            if filename.endswith(".md"):
                file_path = os.path.join(subdir_path, filename)
                
                # Handle filename conflicts
                target_path = os.path.join(target_directory, filename)
                if os.path.exists(target_path):
                    base, ext = os.path.splitext(filename)
                    target_path = os.path.join(target_directory, f"{base}_{subdir}{ext}")
                
                # Move the file to the target directory
                shutil.move(file_path, target_path)
                print(f'Moved: {filename} from {subdir_path} to {target_directory}')

        # After moving files, delete the now-empty subdirectory
        if not os.listdir(subdir_path):  # Check if the directory is empty
            os.rmdir(subdir_path)
            print(f'Deleted empty directory: {subdir_path}')
