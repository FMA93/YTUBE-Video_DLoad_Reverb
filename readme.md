# YouTube Video Reverb Applier

This Python script allows you to download a YouTube video, extract its audio, apply a reverb effect to it, and save the modified audio as an MP3 file. It utilizes the `pytube` library for downloading YouTube videos, the `moviepy` library for video editing, and the `pydub` library for audio processing.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/)

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt


Installing FFmpeg
FFmpeg is crucial for audio and video processing and needs to be installed separately. Follow these steps to download and install FFmpeg:

For Windows: 
You can download a pre-built version of FFmpeg for Windows from the official website: FFmpeg Builds (https://ffmpeg.org/download.html):

- Download the "Windows Builds by shaka" version.
- Extract the downloaded zip file to a folder of your choice.
- Add the path to the folder containing FFmpeg to your system's PATH environment variable.



For Linux (Ubuntu): You can install FFmpeg on Ubuntu using the following command:

sudo apt-get update
sudo apt-get install ffmpeg


For macOS (Homebrew): If you have Homebrew installed, you can install FFmpeg on macOS with the following command:
brew install ffmpeg


Make sure to set the path to the FFmpeg executable in the script as indicated in the code comments.


Usage
Replace 'VIDEO_URL' with the URL of the YouTube video you want to download.

Choose the desired video resolution and format by adjusting the video_stream variable.

Set the file_name and file_extension variables for the downloaded video.

Run the script using the following command:

python youtube_video_reverb.py




The script will download the video, extract its audio, apply a reverb effect, and save the modified audio as output_reverb.mp3.

You can also choose to play the modified audio by uncommenting the relevant line in the script.

The originally downloaded MP4 video file is deleted automatically after the process is complete.



Customization
You can adjust the reverb_duration variable to change the duration of the reverb effect.

Customize the output_file variable to set the name of the output MP3 audio file.

Modify the script to apply other audio effects or edit the video as needed.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute to the project and report any issues or suggestions!


