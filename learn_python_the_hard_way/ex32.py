#lists and for loops

hairs = ['brown', 'blonde', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in weights:
	print "Here are the weights: %d" % number

for i in change:
	print "Here is the change: %r" % i

elements = [] #empty list

for i in range(0,6):
	print "Adding %d to the list" % i
	elements.append(i)
