# Implicit Inheritance

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    def childself(self):
        print "Child function!"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
son.childself()
