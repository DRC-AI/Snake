import curses 

class Snake():

    def __init__(self, max_height, max_width):

        self.max_height = max_height
        self.max_width = max_width
        self.position_y = max_height // 2
        self.position_x = max_width // 2 
        self.body = [[self.position_x, self.position_y], [self.position_x-1, self.position_y]]
        self.head = self.body[0]
        self.direction = curses.KEY_LEFT
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

        if self.position_x < 0:
            self.position_x = self.max_width
        elif self.position_x > self.max_width:
            self.position_x = -1

        elif self.position_y < 0:
            self.position_y = self.max_height
        elif self.position_y > self.max_height:
            self.position_y = -1

        if self.direction == curses.KEY_LEFT:
            self.position_x = self.position_x -1
        elif self.direction == curses.KEY_RIGHT:
            self.position_x = self.position_x +1
        elif self.direction == curses.KEY_UP:
            self.position_y = self.position_y -1
        elif self.direction == curses.KEY_DOWN:
            self.position_y = self.position_y +1

        newHead = [self.position_x,self.position_y]
        
        self.head = newHead
        self.body.insert(0, newHead) 
        self.body.pop(-1)

        return self.body

    def increase_length(self):

        self.body.insert(-1, self.body[-1])

        return self.body
        
    def canbibal(self):

        if self.head in self.body[1:]:
            return True
        