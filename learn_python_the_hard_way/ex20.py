#functions and files

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "Printig whole file:\n"
print_all(current_file)

print "Now let's rewind the file..."
rewind(current_file)

print "Printing first line:\n"
print_a_line(1, current_file)
