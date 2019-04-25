import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), "psVidTex/"))

from movie.movie import Movie

from dummy_movie.first_scene import *
from dummy_movie.second_scene import *

class MovieName(Movie):
    def __init__(self):
        # set constants about the movie here
        Movie.__init__(self)

    # TODO: transition et effets entre scene ?
    def prepare(self):
        self.add_to_timeline(FirstScene, 0, 1, dtype="secondes")
