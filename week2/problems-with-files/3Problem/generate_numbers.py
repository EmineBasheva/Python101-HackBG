import sys
from random import randint

def random_n_integers(n):
    return [str(randint(1, 1000)) for x in range(0, n)]


def main():
    arguments = sys.argv[1:]
    if len(arguments) == 2:
        # print(len(arguments))
        the_file = open(arguments[0], 'w')
        conntents = random_n_integers(int(arguments[1]))
        the_file.write(" ".join(conntents) + "\n")
        the_file.close()
    else:
        print("Incorect arguments")

if __name__ == '__main__':
    main()
