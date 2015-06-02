class Histogram:

    def __init__(self):
        self.__histogram = {}

    def get_dict(self):
        return self.__histogram

    def add(self, name):
        if name not in self.__histogram:
            self.__histogram[name] = 1
        else:
            self.__histogram[name] += 1

    def count(self, name):
        return self.__histogram[name]

    def items(self):
        return self.__histogram.items()