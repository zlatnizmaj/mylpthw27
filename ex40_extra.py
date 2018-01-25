# class without__init__
class EvilTest(object):
    attr = []

evil_test1 = EvilTest()
evil_test2 = EvilTest()

evil_test1.attr.append('NAM')
print "This is result of 'class' without __init__:"
print "\tThis is evil 1 + evil 2: %r + %r" % (evil_test1.attr, evil_test2.attr)

### class with __init__
class GoodTest(object):
    def __init__(self):
        self.attr = []

good_test1 = GoodTest()
good_test2 = GoodTest()

good_test1.attr.append("GAO")

print "\nThis is result of 'class' with __init__:"
print "\tThis is good 1 + good 2: %r + %s" % (good_test1.attr, good_test2.attr)
