# Exercise 6: STRING and TEXT
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said:'%s'." % y

hilariuos = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilariuos

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print e
print w
