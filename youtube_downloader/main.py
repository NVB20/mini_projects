from pytube import YouTube

print("Downloading YouTube video")
video_url = input("Enter YouTUbe video url: ")

YouTube(video_url).streams.first().download()
