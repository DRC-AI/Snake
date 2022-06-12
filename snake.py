import curses 

class Snake():

    def __init__(self, max_height, max_width):

        self.position_y = max_height // 2
        self.position_x = max_width // 2 
        self.body = [ [self.position_x, self.position_y], [self.position_x - 1, self.position_y  ] ]
        self.direction = ""
        self.is_alive = True

    def update_direction(self, keypress):
        
        valid_keys = [
            curses.KEY_LEFT,
            curses.KEY_RIGHT,
            curses.KEY_UP,
            curses.KEY_DOWN
                ]

        reverse_check = {
            curses.KEY_UP : curses.KEY_DOWN,
            curses.KEY_DOWN : curses.KEY_UP,
            curses.KEY_RIGHT : curses.KEY_LEFT,
            curses.KEY_LEFT : curses.KEY_RIGHT
                }
        
        if keypress == reverse_check.get(self.direction):
            return self.direction
        elif keypress not in validKeys:
            return self.direction
        else :
            return self.direction = keypress

    def move_forward(self):

        if self.direction == curses.KEY_LEFT:
            self.position_x = self.position_x - 1
        elif self.direction == curses.KEY_RIGHT:
            self.position_x = self.position_x + 1
        elif self.direction == curses.KEY_UP:
            self.position_y = self.position_y - 1
        elif self.direction == curses.KEY_DOWN:
            self.position_y = self.position_y + 1

        newHead = [self.position_x,self.position_y]
        
        self.body.insert(0, newHead) 
        self.body.pop(-1)

    def increase_length(self):

        self.body.insert(-1, self.body[-1])
        
    def collision_check(self, windowHeight, windowWidth):

        if self.body[0][0] < 1 or self.body[0][0] > windowWidth - 2:
            return False
        if self.body[0][1] < 1 or self.body[0][1] > windowHeight - 2:
            return False
        if self.body[0] in self.body[1:]:
            return False
