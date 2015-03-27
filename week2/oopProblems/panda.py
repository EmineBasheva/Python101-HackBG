# class i instancii
# dunder
# Duck Typing


class Panda:

    def __init__(self, name):
        self.age = 0
        self.weight = 30
        self.name = name

    # mutira6ti metodi
    def grow_up(self):
        self.age += 1

    def eat(self, amount):
        self.weight += amount // 2

    def sleep(self):
        self.weight += 1

    def __add__(self, other):
        return Panda(" ".join([self.name, other.name]))

    def __int__(self):
        return self.weight

    def __str__(self):
        return "I am panda {} and I am {} old".format(self.name, self.age)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name + str(self.weight))

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight


def main():
    ivo = Panda("Ivo")
    new_panda = Panda("puhiii")
    puh_panda = Panda("puhiii")
    ivo.eat(10)
    ivo.grow_up()
    ivo.sleep()
    print(str(ivo), int(ivo))
    ivo.eat(20)
    ivo.grow_up()
    ivo.sleep()
    print(str(ivo), int(ivo))
    ivo.eat(30)
    ivo.grow_up()
    ivo.sleep()
    print(str(ivo), int(ivo))
    big_panda = ivo + new_panda
    print(str(big_panda))
    print(repr(ivo))
    print(new_panda == ivo)
    # print(hash())

if __name__ == '__main__':
    main()
