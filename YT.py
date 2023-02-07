from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)
print(yt.title)


print("views :", yt.views)
print("author :" , yt.author)
print("Video rating :", yt.rating)
yt.bypass_age_gate()
yt = yt.streams.get_highest_resolution()

yt.download("/Users/rikob/Videos/PP")
 
