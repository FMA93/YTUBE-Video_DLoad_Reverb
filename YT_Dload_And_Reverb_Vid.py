import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

from pydub import AudioSegment
from pydub.playback import play

# Replace 'VIDEO_URL' with the URL of the YouTube video you want to download
video_url = 'VIDEO_URL'

# Create a YouTube object
yt = YouTube(video_url)

# Choose the stream with the desired resolution and format
# For example, to get the highest resolution video stream:
video_stream = yt.streams.get_highest_resolution()

# Set the file name and file type (extension) you want for the downloaded video
file_name = 'my_video'  # Replace with your desired file name
file_extension = 'mp4'  # Replace with your desired file type (e.g., mp4, webm, etc.)

# Set the full file path including the file name and extension
file_path = f'{file_name}.{file_extension}'

# Download the video to the specified file path
video_stream.download(output_path='', filename=file_name)

# Replace 'input_video.mp4' with the name of your input MP4 video file
input_file = file_name

# Replace 'output_audio.mp3' with the name you want for the output MP3 audio file
output_name = 'output_audio'
output_file = 'output_audio.mp3'

# Load the video file
video_clip = VideoFileClip(input_file)

# Extract the audio from the video
audio_clip = video_clip.audio

# Save the audio as an MP3 file
audio_clip.write_audiofile(output_file)

# Close the audio and video clips
audio_clip.close()
video_clip.close()

print(f"Video downloaded as {file_path}")
print(f"Conversion complete. Audio saved as {output_file}")




# Replace 'input_audio.mp3' with the name of your input MP3 audio file
input_file = r'C:\Users\malla\OneDrive\Bureaublad\Coding\Python\YoutubeReverb\output_audio.mp3'


# Set the path to the FFmpeg executable so Python can find it when running the script
# You will need to install ffmpeg as it's crucial to do so in order to use the audio conversions within this code

ffmpeg_path = "Set_Your_ffmpeg_Path"

# Load the MP3 file
audio = AudioSegment.from_mp3(input_file)

print('processing audio')

# Apply reverb effect (slowed reverb)
reverb_duration = 5500  # Adjust the reverb duration (in milliseconds) as needed
reverb_audio = audio.fade_in(reverb_duration).fade_out(reverb_duration)

print('processing reverb')


# Export the modified audio to a new MP3 file
output_file = "output_reverb.mp3"
reverb_audio.export(output_file, format="mp3")

print('processing output save')

# Play the modified audio (optional if desired by the end user of the code)
# If you wish to use remove the # and space at the start of the line below this one 
# play(slowed_audio)

# Final confirmation message + removing the originally downloaded Mp4 Youtube Video
print("Reverb has been applied and saved to output.mp3 not that you seem to care.")
print("Guess I might as well also delete the originally downloaded mp4 file since you will never remember to do so!")

os.remove(file_name)