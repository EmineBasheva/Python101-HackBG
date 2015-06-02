import unittest
from song import Song
from song import Length


class TestLength(unittest.TestCase):

    def setUp(self):
        self.len = Length("3:15")

    def test_to_hours(self):
        self.assertEqual(self.len._length, "0:03:15")

    def test_is_valid_length_with_3(self):
      self.assertTrue(self.len._is_valid_length("3:44"))

    def test_with_more_seconds(self):
      with self.assertRaises(Exception):
          length = Length("3:60")

    def test_length_with_hours(self):
      self.assertTrue(self.len._is_valid_length("1:3:44"))

    def test_length_with_days(self):
        with self.assertRaises(Exception):
            length = Length("1:1:3:60")

    def test_get_0_hours(self):
        self.assertEqual(self.len.length(hours=True), 0)

    def test_get_1_hour(self):
        l = Length("1:3:15")
        self.assertEqual(l.length(hours=True), 1)

    def test_get_3_min(self):
        self.assertEqual(self.len.length(minutes=True), 3)

    def test_get_63_min(self):
        l = Length("1:3:15")
        self.assertEqual(l.length(minutes=True), 63)

    def test_get_195_sec(self):
        self.assertEqual(self.len.length(seconds=True), 195)

    def test_get_len(self):
        l = Length("1:3:15")
        self.assertEqual(l.length(), "1:03:15")


class TestMusicLibrary(unittest.TestCase):

    def setUp(self):
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
        self.song2 = Song("Odin", "Manowar", "The Sons of Odin", "1:3:50")
        self.len = Length("3:15")

    def test_is_create_the_class(self):
        self.assertTrue(isinstance(self.song, Song))
    
    def test_test_dunder_str(self):
      self.assertEqual(str(self.song), "Manowar - Odin from The Sons of Odin - 0:03:44")

    def test_dunder_eq_with_True(self):
      song3 = Song("Odin", "Manowar", "The Sons of Odin", "3:44")
      self.assertEqual(self.song, song3)

    def test_dunder_eq_with_False(self):
      song3 = Song("Odin", "Manowar", "The Son of Odin", "3:40")
      self.assertFalse(song3 == self.song)

    

if __name__ == '__main__':
    unittest.main()