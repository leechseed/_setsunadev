import subprocess

def main():
    # Prompt the user for the video URL
    video_url = input("Enter the URL of the video to download: ")
    
    # Full path to yt-dlp executable
    executable_path = r"C:\Users\U01_LEECHSEED\Downloads\yt-dlp.exe"
    
    # Output template to save the file in the specified directory
    output_template = r"C:\Users\U01_LEECHSEED\Downloads\%(title)s.%(ext)s"
    
    # Build the command to run yt-dlp with the given URL and output path
    command = [executable_path, "-o", output_template, video_url]
    
    # Execute the command
    subprocess.run(command)

if __name__ == '__main__':
    main()
