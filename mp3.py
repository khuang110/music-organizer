from mutagen.easyid3 import EasyID3


def read_mp3(song, tag):
    audio = EasyID3(song)
    return audio[tag]



