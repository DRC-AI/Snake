import random

class Score():

    def __init__(self, max_height, max_width):

        self.max_height = max_height
        self.max_width = max_width
        self.position_x = random.randint(1, self.max_width -1)
        self.position_y = random.randint(1, self.max_height -1)
        self.score = 0
        self.combo = 1 

    def increase(self):

        base_score = 100
        combo_score = base_score * self.combo
        self.score = int(self.score + combo_score)
    
    def get_position(self):

        return [self.position_x, self.position_y]

    def generate_point(self):

        self.position_x = random.randint(1, self.max_width -1)
        self.position_y = random.randint(1, self.max_height -1)

        return (self.position_x, self.position_y)