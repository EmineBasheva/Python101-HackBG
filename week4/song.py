import datetime


class Length:
    def __init__(self, length):
        if not self._is_valid_length(length):
            raise Exception("invalid length")
        self._length = self.to_have_hours(length)

    def to_have_hours(self, length):
        parts_of_length = length.split(":")

        if len(parts_of_length) == 2:
            hours = ["0"]
            hours.extend(parts_of_length)
            parts_of_length = hours

        s = int(parts_of_length[2])
        m = int(parts_of_length[1])
        h = int(parts_of_length[0])

        return str(datetime.timedelta(hours=h, minutes=m, seconds=s))

    def _is_valid_length(self, length):
        parts_of_length = length.split(":")
        cond_len_3 = len(parts_of_length) == 3
        cond_len_2 = len(parts_of_length) == 2

        cond_length = all(int(part) < 60 and int(part) > -1 for part in parts_of_length)
        return cond_length and (cond_len_2 or cond_len_3)

    def length(self, hours=False, minutes=False, seconds=False):
        parts_of_length = self._length.split(":")

        h = int(parts_of_length[0])
        m = int(parts_of_length[1])
        s = int(parts_of_length[2])

        if not(hours) and not(minutes) and not(seconds):
            return self._length
        elif hours:
            return h
        elif minutes:
            return h * 60 + m
        elif seconds:
            return (h * 60 + m) * 60 + s

    def __str__(self):
        return self.length()

    def __eq__(self, other):
        self_parts = self._length.split(":")
        other_parts = other._length.split(":")

        return all(int(self_parts[i]) == int(other_parts[i]) for i in range(0, 3))
            


class Song:

    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = Length(length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title,
                                             self.album, self._length)
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        cond_title = self.title == other.title
        cond_artist = self.artist == other.artist
        cond_album = self.album == other.album
        cond_length = self._length == other._length
        return cond_title and cond_artist and cond_album and cond_length

    def __hash__(self):
        return hash(self.__str__())

    def length(self, hours=False, minutes=False, seconds=False):
        return self._length.length(hours=hours, minutes=minutes, seconds=seconds)
