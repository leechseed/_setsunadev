import os
import yaml
import re
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter category is CORE with possible values
query_core_values = [
    "NV-3405 Narrative Voice and Point of View",
    "NA-3402 Narration and Narrator Analysis",
    "CH-3302 Characterization",
    "SN-3504 Semiotics of Narrative",
    "HN-3701 Holistic Narrative Analysis",
    "FM-3506 Function and Motif Analysis",
    "FO-3403 Focalization",
    "NE-3509 Narrative Ethics and Ideology",
    "SD-3401 Story vs. Discourse (Fabula vs. Sjuzhet)",
    "NS-3301 Narrative Structure",
    "DM-3503 Diegesis and Mimesis",
    "TT-3404 Time and Temporality",
    "CL-3406 Narrative Coherence and Logic",
    "INT-3502 Intertextuality",
    "NR-3507 Narratee and Implied Reader",
    "AS-3601 Advanced Semiotics and Symbolic Interpretation",
    "TN-3602 Transmedia Narratology",
    "TI-3702 Theoretical Integration",
    "MT-3508 Metalepsis and Narrative Transgression",
    "FM-3506 Function and Motif Analysis",  # Duplicate entries can be removed if necessary
    "SN-3504 Semiotics of Narrative",
    "HN-3701 Holistic Narrative Analysis",
    # Add all other CORE values from your data here
    # ...
]

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"YAML error: {e}")
    return None

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        filepath = os.path.join(input_directory, filename)

        # Read the file content
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            continue

        # Extract the YAML frontmatter
        yaml_data = extract_yaml_frontmatter(content)
        
        if yaml_data and 'CORE' in yaml_data:
            # Normalize and check if the value in 'CORE' is one of the specified categories
            core_value = yaml_data['CORE'].strip()
            if core_value in query_core_values:
                # Extract the code part for folder name (e.g., "NV-3405" from "NV-3405 Narrative Voice and Point of View")
                core_code = core_value.split()[0]

                # Create the output directory based on the CORE code
                output_directory = os.path.join(base_output_directory, core_code)
                os.makedirs(output_directory, exist_ok=True)

                # Move the file to the appropriate output directory
                try:
                    shutil.move(filepath, os.path.join(output_directory, filename))
                    print(f'Moved: {filename} to {output_directory}')
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")
            else:
                print(f'Unrecognized CORE value in file: {filename}')
        else:
            print(f'No CORE field in file: {filename}')
