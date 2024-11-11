from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a Tkinter root window to hold the dialog
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask for YouTube URL
url = simpledialog.askstring("YouTube Downloader", "Enter YouTube Video URL:")

if url:
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Get highest resolution stream
        video.download()  # Download video to current directory
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video.\n{e}")
else:
    messagebox.showwarning("Input Needed", "No URL provided.")

# Close the Tkinter window
root.destroy()
