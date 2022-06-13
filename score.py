import random

class Score():

    def __init__(self, max_height, max_width):
        self.positionx = 0
        self.positiony = 0
        self.max_height = max_height
        self.max_width = max_width
        self.score = 0

    def increase(self):

        self.score = self.score + 100

    def position(self):

        return (self.positionx, self.positiony)

    def generate_point(self):

        self.positionx = random.randint(0, self.max_width)
        self.positiony = random.randint(0, self.max_height)