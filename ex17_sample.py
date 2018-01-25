#truncate() method for file handling
#fileObject.truncate([size])

#Open a fileObject
fo = open("foo.txt","r+")
print "Name of the file: ", fo.name

line = fo.readline()
print "Read Line: %s" % line

# Now truncate remaining file.
fo.truncate()

#Try to read file now
line = fo.readline()
print "Read Line: %s" % line

#Close opened file
fo.close()

value = "one two three"
# Truncate the string to 3 characters.
first = value [0:3]
print first + "."
# Truncate the string to 7 characters.
second = value [0:7]
print second + "."

#Omit the first 0 in the slice syntax
letters = "abcdef"
#...This truncates the string.
print letters
first_part = letters[:3]
print "First part (3char) of letters: ", first_part
