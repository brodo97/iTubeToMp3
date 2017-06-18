import sqlite3, os
import moviepy.editor as mp

available, videos = [], []

try:
    conn = sqlite3.connect('DB/playTube.db')
    for row in conn.execute('SELECT id,title FROM videos'):
        videos.append(row)
except Exception as e:
    os.system("mkdir DB")
    print "No 'playTube.db' file found! Copy your iTube database in the DB folder"
    exit()

try:
    available = os.listdir("./mp4/")
except Exception as e:
    os.system("mkdir mp4")
    print "mp4 folder doesn't exist. I've created it for you! Now move you file in it"
    exit()

for video in videos:
    if video[0]+".mp4" in available:
        try:
            clip = mp.VideoFileClip("mp4/"+video[0]+".mp4")
            clip.audio.write_audiofile("mp3/"+video[1]+".mp3")
        except Exception as e:
            os.system("mkdir mp3")
            print "Conversion error! Does mp3 folder exist? Nevermind, I've created it for you"
            exit()
