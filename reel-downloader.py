from pytube import YouTube

def youtube(url, format, resolution):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Select the stream with the desired resolution and file format (e.g., 720p MP4)
        stream = yt.streams.filter(progressive=True, file_extension=format, resolution=resolution).first()

        # Download the video
        stream.download()

        print("Video downloaded successfully as MP4.")

    except Exception as e:
        print("An error occurred:", str(e))

youtube("https://www.youtube.com/shorts/5WqLjXTuvyU", "", )