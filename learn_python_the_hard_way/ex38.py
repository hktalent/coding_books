#working with lists and loops

ten_things = "apples oranges crows telephone light sugar"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "banana", "bike"]

print "Currently stuff has: ", stuff

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)

print "Now stuff has: ", stuff
