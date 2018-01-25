# Modules, Classes and Objects
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


HAPPY_BDAY = Song(["Happy birth day to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

BULL_ON_PARADE = Song(["They rally around the family",
                       "With pockets full of shells"])

HAPPY_BDAY.sing_me_a_song()
print '-' * 35
BULL_ON_PARADE.sing_me_a_song()


def in_ra(string):
    print string


STR = "nam"
in_ra(STR)
