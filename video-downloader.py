

from pytube import YouTube

link = input('Enter link: ')
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)
print("Duration:", yt.length)

yd = yt.streams.get_highest_resolution()

yd.download('./video-downloads')



