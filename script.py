from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import sys
from youtubesearchpython import VideosSearch


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl': '%(title)s.%(ext)s',
}

videosSearch = VideosSearch(sys.argv[1], limit = 10)
results = videosSearch.result()['result']

for video in results:
    print('Found "' + video['title'] + '" with duration: ' + video['duration'])
    ok = input('Y to download, N to next: ')
    while ok.lower() != 'y' and ok.lower() != 'n':
        ok = input('Y to download, N to next: ')
    ok = ok.lower()
        
    if ok == 'y':
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(video['link'])
        print('Done')
        sys.exit()
    else:
        continue

print('No videos found')
