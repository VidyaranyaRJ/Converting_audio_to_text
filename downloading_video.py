import pytube

# set the YouTube URL
url = 'https://www.youtube.com/watch?v=CqbOIqk8gxE'

# create a YouTube object
yt = pytube.YouTube(url)

# get the first stream with the "mp4" format
mp4_stream = yt.streams.filter(file_extension='mp4').first()

# download the video to the current working directory
mp4_stream.download()
