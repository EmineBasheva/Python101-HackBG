from song import Song
import datetime
from random import randint
import random
from tabulate import tabulate


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.all_songs = []
        self.current_song = None
        self.index_current_song = -1
        self.all_shuffle = []

    def add_song(self, song):
        if not isinstance(song, Song):
            print(song)
            raise TypeError
        self.all_songs.append(song)

    def remove_song(self, song):
        if not isinstance(song, Song):
            raise TypeError
        self.all_songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total_len = datetime.timedelta(seconds=0)

        for song in self.all_songs:
            s = song.length(seconds=True)
            total_len = total_len + datetime.timedelta(seconds=s)

        return str(total_len)

    def artists(self):
        all_artists = [song.artist for song in self.all_songs]
        return {artist: all_artists.count(artist) for artist in all_artists}

    def shuffle_songs(self):

        while len(self.all_shuffle) < len(self.all_songs):
            random_choice = random.choice(self.all_songs)
            if random_choice not in self.all_shuffle:
                self.all_shuffle.append(random_choice)

        return self.all_shuffle

    def get_random_song(self):
        if not(len(self.all_shuffle) > 0):
            self.all_shuffle = self.shuffle_songs()
        return self.all_shuffle[self.index_current_song]

    def next_song(self):
        if len(self.all_songs) > 0:
            self.index_current_song += 1
            if self.index_current_song == len(self.all_songs):
                if self.repeat:
                    self.index_current_song = 0
                else:
                    raise Exception('End of playlist')
            if self.shuffle:
                self.current_song = self.get_random_song()
            else:
                self.current_song = self.all_songs[self.index_current_song]

        return self.current_song

    def pprint_playlist(self):
        pplaylist = [[song.artist, song.title, song.length()] for song in self.all_songs]
        headers = ["Artist", "Title", "Length"]
        print(tabulate(pplaylist, headers, tablefmt="rst"))

    
