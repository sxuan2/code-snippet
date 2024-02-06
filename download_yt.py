from pytube import YouTube

# YouTube video URL
video_url = input('the url...\n')

# Specify the download location
download_location = r'G:'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

# Download the video to the specified location
video_stream.download(output_path=download_location)

print("Download complete!")
