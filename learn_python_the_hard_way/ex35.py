#testing choices and arrays

def monster_room():
	print "You enter the monster room."
	print "Do you flee, or fight?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "fight" in choice:
		dead("You got eaten by the monster!")
	else:
		monster_room()

def gold_room():
	print "You get all of the gold!"
	dead("You die of greed!")

def dead(message):
	print "You have died. %r" % message
	exit(0)

def start():
	print "You see two doors"
	print "One to the right, one to the left"
	print "Which one do you enter?"

	choice = raw_input("> ")

	if "left" in choice:
		monster_room()
	elif "right" in choice:
		gold_room()
	else:
		start()

start()
