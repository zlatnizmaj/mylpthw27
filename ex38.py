# Doing things to lists
ten_thing = "Apples Oranges Crows Telephone Light Sugar"

print ten_thing
print "Wait there's not 10 thing in that list, let's fix that."

stuff = ten_thing.split(' ')

print stuff

more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print more_stuff, "\n"
print more_stuff[3:4]
while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop() lay tu cuoi len from the end list to first
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now.\n" % len(stuff)

print "There we go (stuff):\n", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # whoa! fancy
print stuff.pop()
print stuff[3:5]
print stuff
print ' '.join(stuff)  # what? cool! join() ghep cac item cua list thanh string cach nhau bang ' '.
print '_'.join(stuff[3:5])  # super stellar! cach nhau bang "
#print join('+', stuff) # NameError: name 'join' is not defined

# ' '.join(things) same as join(' ', things)
