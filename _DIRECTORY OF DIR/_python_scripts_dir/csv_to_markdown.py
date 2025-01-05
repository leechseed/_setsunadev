import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Create a dialog box to select the CSV file
def select_csv_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Bring the dialog box to the front
    file_path = askopenfilename(filetypes=[("CSV Files", "*.csv")], title="Select CSV File")
    root.destroy()
    return file_path

# Prompt user to select a file
csv_file = select_csv_file()

if csv_file:
    # Load the selected CSV file
    df = pd.read_csv(csv_file)

    # Convert to Markdown table
    markdown_table = df.to_markdown(index=False)

    # Save to a Markdown file
    output_file = csv_file.replace(".csv", ".md")  # Save with the same name as the CSV but with .md extension
    with open(output_file, "w") as f:
        f.write(markdown_table)

    print(f"Markdown table saved as {output_file}")
else:
    print("No file selected. Script aborted.")
