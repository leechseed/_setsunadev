import os
import yaml
import re
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='file_mover.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Use the script directory as both the input and base output directory
input_directory = script_directory
base_output_directory = script_directory

# YAML frontmatter valid categories (TIER)
valid_tiers = ["Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5", "Tier 6"]

# YAML frontmatter valid categories (CORE)
valid_cores = {
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
    "NLE-3501 Narrative Levels and Embedding",
    "PA-3303 Plot and Event Analysis",
    "GT-3505 Genre and Narrative Typology",
}

# Enable dry run mode (set to False to perform actual file moves)
dry_run = False

# Function to extract YAML frontmatter
def extract_yaml_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            logging.error(f"YAML error: {e}")
            return None
    return None

# Function to sanitize folder names
def sanitize_folder_name(name):
    # Remove or replace characters that are invalid in folder names
    # For simplicity, we'll replace them with underscores
    sanitized = re.sub(r'[\/\\\:\*\?\"\<\>\|]', '_', name)
    return sanitized

# Function to extract CORE code
def extract_core_code(core_value):
    # Assuming CORE value starts with the code followed by a space and description
    parts = core_value.split()
    if parts:
        return parts[0]  # e.g., "NV-3405"
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
            logging.error(f"Error reading file {filename}: {e}")
            print(f"Error reading file {filename}: {e}")
            continue

        # Extract the YAML frontmatter
        yaml_data = extract_yaml_frontmatter(content)

        # Debug print
        print(f'Processing file: {filename}')
        logging.info(f'Processing file: {filename}')

        if yaml_data:
            # Extract TIER and CORE from YAML frontmatter
            tier_value = yaml_data.get('TIER', '').strip()
            core_value = yaml_data.get('CORE', '').strip()

            # Validate TIER and CORE values
            if tier_value in valid_tiers:
                if core_value in valid_cores:
                    core_code = extract_core_code(core_value)
                    if core_code:
                        # Sanitize CORE name for folder naming
                        sanitized_core = sanitize_folder_name(core_value)

                        # Create the output directory based on TIER and CORE
                        output_directory = os.path.join(base_output_directory, tier_value, sanitized_core)
                        if not os.path.exists(output_directory):
                            if dry_run:
                                logging.info(f'[Dry Run] Would create directory: {output_directory}')
                                print(f'[Dry Run] Would create directory: {output_directory}')
                            else:
                                try:
                                    os.makedirs(output_directory, exist_ok=True)
                                    logging.info(f'Created directory: {output_directory}')
                                    print(f'Created directory: {output_directory}')
                                except Exception as e:
                                    logging.error(f"Error creating directory {output_directory}: {e}")
                                    print(f"Error creating directory {output_directory}: {e}")
                                    continue

                        # Move the file to the appropriate output directory
                        destination = os.path.join(output_directory, filename)
                        if dry_run:
                            logging.info(f'[Dry Run] Would move: {filename} to {output_directory}')
                            print(f'[Dry Run] Would move: {filename} to {output_directory}')
                        else:
                            try:
                                shutil.move(filepath, destination)
                                logging.info(f'Moved: {filename} to {output_directory}')
                                print(f'Moved: {filename} to {output_directory}')
                            except Exception as e:
                                logging.error(f"Error moving file {filename}: {e}")
                                print(f"Error moving file {filename}: {e}")
                    else:
                        logging.warning(f'Invalid CORE format in file: {filename}')
                        print(f'Invalid CORE format in file: {filename}')
                else:
                    logging.warning(f'Unrecognized CORE value in file: {filename}')
                    print(f'Unrecognized CORE value in file: {filename}')
            else:
                logging.warning(f'Unrecognized TIER value in file: {filename}')
                print(f'Unrecognized TIER value in file: {filename}')
        else:
            logging.warning(f'No valid YAML data in file: {filename}')
            print(f'No valid YAML data in file: {filename}')
