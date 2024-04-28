from sys import argv

from pytube import YouTube

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)
print("Duration:", yt.length)

yd = yt.streams.get_highest_resolution()

yd.download('./downloads')



