#more string testing

x = "There are %d types of people" % 10
binary = "binary"
doNot = "don't"
y= "Those who know %s and those who %s" % (binary, doNot)

print x
print y

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"

print jokeEvaluation % hilarious

l = "This is the left side..."
r = "and This is the right side."

print l + r
