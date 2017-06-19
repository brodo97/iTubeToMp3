"""
This tool need the following folders:
    DB
    mp4
    mp3
Put the database in DB folder
Put videos in mp4 folder
"""

import sqlite3, os, unicodedata
import moviepy.editor as mp

available, videos = [], []

root = os.listdir("./")
if not "mp4" in root:
    os.system("mkdir mp4")
if not "mp3" in root:
    os.system("mkdir mp3")
if not "DB" in root:
    os.system("mkdir DB")

try:
    conn = sqlite3.connect('DB/playTube.db')
    for row in conn.execute('SELECT id,title FROM videos'):
        videos.append(row)
except Exception as e:
    print "No 'playTube.db' file found! Copy your iTube database in the DB folder"
    exit()

try:
    available = os.listdir("./mp4/")
except Exception as e:
    print "Videos check error!"
    exit()

q = raw_input("Remove source video after conversion? Y/N: ")
remove = False;

if q.lower() == "y":
    remove = True

notConverted = []

for video in videos:
    if video[0]+".mp4" in available:
        try:
            clip = mp.VideoFileClip("./mp4/"+video[0]+".mp4")
            name = unicodedata.normalize('NFKD', video[1]).encode('ascii', 'ignore')
            clip.audio.write_audiofile("./mp3/"+name+".mp3")
            
            if remove:
                os.system("rm mp4/"+video[0]+".mp4")
        except Exception as e:
            notConverted.append(video[0]+".mp4 -> "+video[1]+".mp3")
            print "Conversion error! "+video[0]+".mp4 -> "+video[1]+".mp3"

if len(notConverted)==0:
    print "Everything OK! All videos converted!"
else:
    for video in notConverted:
        print video
