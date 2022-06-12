import random

class Score():

    def __init__(self, window):
        self.positionx = 0
        self.positiony = 0
        self.score = 0
        self.window = window

    def increase(self):

        self.score = self.score + 100

    def position(self):

        return (self.positionx, self.positiony)

    def generate_point(self, max_width, max_height):

        self.positionx = random.randint(0, max_width)
        self.positiony = random.randint(0, max_height)