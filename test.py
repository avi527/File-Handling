class Song(object):
    def __init__(self, name):
        self.name = name

songNames = ['song1', 'song2', 'song3']

songs = []
for name in songNames:
    songs.append(Song(name))
print(songs)
