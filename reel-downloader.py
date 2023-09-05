from pytube import YouTube

import requests

class Youtube():
    def convert(self, url, format, resolution):
        try:
            # Create a YouTube object
            yt = YouTube(url)

            # Select the stream with the desired resolution and file format (e.g., 720p MP4)
            stream = yt.streams.filter(progressive=True, file_extension=format, resolution=resolution).first()

            # Download
            stream.download()

            print("Youtube video downloaded successfully")

        except Exception as e: # Error handling
            print("An error occurred.", str(e))

# Create an instance of ReelDownloader
downloader = Youtube()
# downloader.youtube_convert("https://www.youtube.com/shorts/5WqLjXTuvyU", "mp4", "720p")


class Media():
    def convert(video_url):
        url = "https://all-media-downloader.p.rapidapi.com/rapid_download/download"

        payload = { "url": f"{video_url}" }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "d841669306mshbe4832b0a2b908fp1cb62ejsn48da473bd1df",
            "X-RapidAPI-Host": "all-media-downloader.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, headers=headers)

        print(response.json())

Media.convert("https://www.instagram.com/p/CwgGF6rrrDg/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==")