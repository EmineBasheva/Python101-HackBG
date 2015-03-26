import sys


def main():
	argument = sys.argv[1:]

	the_file = open(argument[0], 'r')
	contents = the_file.read()
	the_file.close()
	sum_integers = sum([int(num) for num in contents.split(" ")])

	print(sum_integers)


if __name__ == '__main__':
	main()
