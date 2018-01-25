# Names, Variables, Code, Functions
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args i actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothing'."

print_two("Nam", "Nguyen")
print_two_again("Mr", "Gao")
print_one("First!")
print_none()
