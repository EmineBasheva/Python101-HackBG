import unittest
from song import Song
from play_list import Playlist

class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.song2 =  Song("Odin", "Manowar", "The Sons of Odin", "1:3:50")
    
    def test_add_song(self):
        self.code_songs.add_song(self.song)
        self.assertEqual(self.code_songs.all_songs, [self.song])

    def test_add_songs(self):
        self.code_songs.add_songs([self.song, self.song2])
        self.assertEqual(self.code_songs.all_songs, [self.song, self.song2])

    def test_remove_song(self):
        self.code_songs.add_songs([self.song, self.song2])
        self.code_songs.remove_song(self.song2)
        self.assertEqual(self.code_songs.all_songs, [self.song])

    def test_total_length_1_7_34(self):
        self.code_songs.add_songs([self.song2, self.song])
        self.assertEqual(self.code_songs.total_length(), '1:07:34')

    def test_artists(self):
        self.code_songs.add_songs([self.song2, self.song])
        self.assertEqual(self.code_songs.artists(), {self.song2.artist: 2})

    def test_shuffle_songs(self):
        self.code_songs.add_songs([self.song, self.song2])
        print(self.code_songs.shuffle_songs())

    def test_next_song(self):
        song1 = Song("Odin", "Manowar", "The Sons of Odin", "2:3:12")
        self.code_songs.add_songs([self.song2, self.song, song1])
        print(self.code_songs.next_song(), self.code_songs.index_current_song)
        print(self.code_songs.next_song(), self.code_songs.index_current_song)
        print(self.code_songs.next_song(), self.code_songs.index_current_song)
        print(self.code_songs.next_song(), self.code_songs.index_current_song)

    def test_pprint_playlist(self):
        song1 = Song("Odin", "Manowar", "The Sons of Odin", "2:3:12")
        self.code_songs.add_songs([self.song2, self.song, song1])
        self.code_songs.pprint_playlist()

if __name__ == '__main__':
    unittest.main()