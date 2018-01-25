# Functions and Files
from sys import argv

script, input_file = argv

print "This is script %s\n" % script


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline().splitlines()


current_file = open(input_file)

print "First let's print the whole file:"

print_all(current_file)

print "\nNow let's rewind, kind of like a tape."
rewind(current_file)

print "\nLet's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
