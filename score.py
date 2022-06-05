import random

class Score():

    def __init__(self, window):
        self.positionx = 0
        self.positiony = 0
        self.score = 0
        self.window = window
    
    def is_point(self, snakePosition):
        '''checks if the snake head overlaps with point position'''
        
        pointPosition = self.get_position()

        if pointPosition == snakePosition:
            return True
        else :
            return False

    def increase_score(self):
        '''Increases score by 1'''

        self.score = self.score + 100



    def get_position(self):
        '''This functions returns position in a tuple'''

        position = [ self.positionx , self.positiony ]

        return position

    def generate_point(self):
        '''Generates a point with random position'''

        y, x = self.window.getmaxyx()
       
        self.positionx = random.randint(1, x -2)
        self.positiony = random.randint(1, y -2)

    def render(self, window):
        '''Renders point in passed window'''

        window.addstr(self.positiony, self.positionx, "*")
    
