import pafy
url=input("your youtube video link: ")
video=pafy.new(url)
print(video)
stream= video.videostreams
print(stream)
#i=0
best = video.getbest()
print(best.get_filesize())
#while i<len(stream):
#    print(i+1,stream[i])
 #   i=i+1
#best.download()
