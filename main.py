import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Directory containing MP4 files
input_dir = 'Video'

# Output directory to save MP3 files
output_dir = 'Audio'

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an MP4 file
    if filename.endswith('.mp4'):
        # Construct the full file paths for the input and output files
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename[:-4] + '.mp3')
        
        # Use moviepy to convert the MP4 file to an MP3 file with a bitrate of 128 kbps
        video = VideoFileClip(input_file)
        audio = video.audio
        audio.write_audiofile(output_file, bitrate='128k')
        
        # Print a message to indicate that the conversion is complete
        print(f"Converted {input_file} to {output_file}")
