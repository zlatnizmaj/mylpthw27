# function
def add_numbers(maxList):
    i = 0
    numbers = []
    while i < maxList:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 2
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i
    return numbers


def print_numbers(numbers):
    print "The list of numbers is: "
    for num in numbers:
        print num


print "Please, enter the max of list: "
broj = int(raw_input("> "))

numbers = add_numbers(broj)

print_numbers(numbers)
