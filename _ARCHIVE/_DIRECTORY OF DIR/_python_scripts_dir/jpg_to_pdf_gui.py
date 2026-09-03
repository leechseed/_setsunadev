import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_jpgs_to_pdf(source_folder, output_pdf):
    # Get all jpg and jpeg files in the source folder
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    # Sort the files alphabetically
    jpg_files.sort()
    
    if not jpg_files:
        messagebox.showerror("No Images Found", "No JPG or JPEG files were found in the selected folder.")
        return
    
    image_list = []
    
    for file_name in jpg_files:
        file_path = os.path.join(source_folder, file_name)
        try:
            img = Image.open(file_path)
            # Convert all images to RGB (necessary for PDF conversion)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            image_list.append(img)
        except Exception as e:
            messagebox.showwarning("Image Open Error", f"Error opening {file_name}: {e}")
    
    if image_list:
        try:
            first_image = image_list.pop(0)
            first_image.save(
                output_pdf,
                "PDF",
                resolution=100.0,
                save_all=True,
                append_images=image_list
            )
            messagebox.showinfo("Success", f"Successfully created PDF:\n{output_pdf}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Error saving PDF: {e}")
    else:
        messagebox.showerror("No Images", "No valid images were found to save.")

def select_folder_and_convert():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select the source folder
    source_folder = filedialog.askdirectory(title="Select Folder Containing JPG/JPEG Files")
    
    if not source_folder:
        messagebox.showinfo("No Folder Selected", "Operation cancelled. No folder was selected.")
        return
    
    # Prompt the user to choose where to save the output PDF
    output_pdf = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF As"
    )
    
    if not output_pdf:
        messagebox.showinfo("No Save Location", "Operation cancelled. No save location was selected.")
        return
    
    convert_jpgs_to_pdf(source_folder, output_pdf)

if __name__ == "__main__":
    select_folder_and_convert()
