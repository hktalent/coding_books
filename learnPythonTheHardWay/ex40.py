class Song(object):

        def __init__(self, lyrics):
                self.lyrics = lyrics

        def sing_me_a_song(self):
                for line in self.lyrics:
                        print line

bulls_on_parade = Song(["They rally around the family", "With a pocket full of shells"])

bulls_on_parade.sing_me_a_song()
