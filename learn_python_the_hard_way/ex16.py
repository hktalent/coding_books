from sys import argv

script, filename = argv

print "were going to erase %r" % filename
print "if you dont want this type ctrl+c"
print "if you do want that, hit return"

raw_input("?")

print "opening file..."
target = open(filename, 'w')

print "truncating file %r" % filename
target.truncate()

print "now i am going to ask you for three lines"

line1 = raw_input("input 1: ")
line2 = raw_input("input 2: ")
line3 = raw_input("input 3: ")

print "im going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "...and we are done!"
target.close()
