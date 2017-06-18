# iTube video to mp3 converter
iTube is a useful YouTube's video downloader for Android.

## The problem:
If you use iTube for music you don't need the video! But, iTube store videos' information inside a database and change the original name with a different one like this one: '3ou8PXfDhFI.mp4'.

## The solution:
This tool check the database and convert videos in mp3s with the original name.

## Requirement
For Python 2.7

This tool require the database inside the application's folder. You can easily find it in your archive and move it in DB folder.

The database's name is playTube.db

It also require videos, just move it in mp4 folder. The output mp3s will be converted inside mp3 folder.

You also need to install a Python's library named: 'moviepy'
```bash
  $ sudo pip install moviepy
```
## Execution
Just run it by typing:

```bash
  $ python iTube.py
```
or
```bash
  $ python2.7 iTube.py
```
