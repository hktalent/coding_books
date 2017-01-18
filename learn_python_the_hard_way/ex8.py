# formatters and strings
# note that %r is used for debugging, whereas %s is usually used otherwise

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
