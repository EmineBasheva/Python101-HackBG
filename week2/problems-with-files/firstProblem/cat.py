import sys


# for arg in sys.argv:
# 	print(arg)

filename = open("text_file.txt")

content = filename.read()
lines = content.split("\n")

for line in lines:
	print(line)

filename.close()
