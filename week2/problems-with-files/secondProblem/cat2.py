import sys


def has_arguments():
	return len(sys.argv[1:]) > 0

def main():
	arguments = sys.argv[1:]
	if has_arguments():
		for argument in arguments:
			the_file = open(argument, "r")
			content = the_file.read()
			print(content)
			the_file.close()
	else:
		print("There are no arguments :(")

if __name__ == '__main__':
	main()
	