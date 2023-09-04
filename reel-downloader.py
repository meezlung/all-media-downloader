from pytube import YouTube
from instascrape import Reel

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ReelDownloader():
    def youtube_convert(self, url, format, resolution):
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
downloader = ReelDownloader()

# downloader.youtube_convert("https://www.youtube.com/shorts/5WqLjXTuvyU", "mp4", "720p")