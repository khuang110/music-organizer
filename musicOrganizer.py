import os
import shutil
from mp3 import read_mp3
from pprint import pprint


# Check if folder exist and make new one
def create_folder(cwd, tag):
    tag2 = remove_tags(tag)
    path = os.path.join(cwd, tag2)
    if not os.path.isdir(path):
        os.mkdir(tag2)
    return path


# Remove unwanted stuff from tag
def remove_tags(tag):
    rep = {"'": "", " ": "_", "[": "", "]": ""}
    tag2 = str(tag)
    for i, j in rep.items():
        tag2 = tag2.replace(i, j)
    return tag2


if __name__=="__main__":
    cwd = os.getcwd()
    artists = []
    for song in os.listdir(cwd):
        if song.endswith(".mp3"):
            artist = read_mp3(song, "artist")
            p = create_folder(cwd, artist)
            print(remove_tags(artist))
            artists.append(remove_tags(artist))
            shutil.move(os.path.join(cwd, song), p)
            # Change dir to artist dir
            os.chdir(p)

    for artist in os.listdir(cwd):
        cwd2 = os.getcwd()
        #print(cwd2)
        #pprint(artists)
        if artist in artists:
            for s in os.listdir(cwd2):
                if s.endswith(".mp3"):
                    album = read_mp3(s, "album")
                    a = create_folder(cwd2, s)
                    print(a)
                    shutil.move(os.path.join(cwd2, s), a)
