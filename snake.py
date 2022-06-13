import curses 

class Snake():

    def __init__(self, max_height, max_width):

        self.max_height = max_height
        self.max_width = max_width
        self.position_y = max_height // 2
        self.position_x = max_width // 2 
        self.body = [ [self.position_x, self.position_y], [self.position_x - 1, self.position_y  ] ]
        self.direction = ""
        self.is_alive = True
    
    def reversed(self, key):

        reverse_check = {
            curses.KEY_UP : curses.KEY_DOWN,
            curses.KEY_DOWN : curses.KEY_UP,
            curses.KEY_RIGHT : curses.KEY_LEFT,
            curses.KEY_LEFT : curses.KEY_RIGHT
                }
        
        return key == reverse_check.get(self.direction)
    
    def valid_key(self, key):
        
        valid_keys = [
            curses.KEY_LEFT,
            curses.KEY_RIGHT,
            curses.KEY_UP,
            curses.KEY_DOWN
                ]
        
        return key in valid_keys

    def update_direction(self, key):

        if not self.reversed(key) and self.valid_key(key):
            self.direction = key
            return self.direction
        else:
            return self.direction
        
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

        return self.body

    def increase_length(self):

        self.body.insert(-1, self.body[-1])

        return self.body
        
    def collision_check(self, position_x, position_y):

        if position_x < 1 or position_x > self.max_height:
            return True
        elif position_y < 1 or position_y > self.max_width:
            return True
        elif (position_x, position_y) in self.body[1:]:
            return True
        else:
            return False
