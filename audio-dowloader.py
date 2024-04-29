import os
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=XoiOOiuH8iI'
video = YouTube(url)

print('Title: ', video.title)
print('Downloading...')

# Download the audio stream
audio_stream = video.streams.filter(only_audio=True).first()
outpath = audio_stream.download()

# Rename the downloaded file to have a .mp3 extension
new_name = os.path.splitext(outpath)[0] + '.mp3'
os.rename(outpath, new_name)
print('Done')
