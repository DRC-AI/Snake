import curses 

class Snake():

    def __init__(self, game_window):
        '''Sets default settings to snake object'''

        self.position_y, self.position_x = game_window.getmaxyx()

        #centers the position of snake to middle of passed window
        self.position_y = self.position_y // 2
        self.position_x = self.position_x // 2 

        #initializes the snake body list using its position properties
        self.body = [ [self.position_x, self.position_y], [self.position_x - 1, self.position_y  ] ]
        #initializes direction
        self.direction = ""

        #initializes is_alive property to True
        self.is_alive = True

        #initializes game_window property to passed window
        self.game_window = game_window

    def prevent_reverse(self, keypress) :
        '''Makes sure the user cant reverse direction,
        and can only turn or continue forward.'''

        notAllowed = {
                curses.KEY_UP : curses.KEY_DOWN,
                curses.KEY_DOWN : curses.KEY_UP,
                curses.KEY_RIGHT : curses.KEY_LEFT,
                curses.KEY_LEFT : curses.KEY_RIGHT
                }
        
        if keypress == notAllowed.get(self.direction):
            return False
        else:
            return True

    def update_direction(self, keypress):
        '''Used to update direction of head.
        Needs keypress in curse.KEY_DIRECTION format.'''

        #Only updates if key i valid
        validKeys = [ curses.KEY_LEFT,curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN ]
        
        if self.prevent_reverse(keypress):

            if keypress not in validKeys:
                return self.direction
            else :
                self.direction = keypress
                return self.direction
        else:
            return self.direction

    def move_forward(self):
        '''Makes the snake move forward 1 step in the facing direction
        and updates the body list'''
        
        if self.direction == curses.KEY_LEFT:
            self.position_x = self.position_x - 1
        elif self.direction == curses.KEY_RIGHT:
            self.position_x = self.position_x + 1
        elif self.direction == curses.KEY_UP:
            self.position_y = self.position_y - 1
        elif self.direction == curses.KEY_DOWN:
            self.position_y = self.position_y + 1

        self.update_body(self.position_x, self.position_y)

    def update_body(self, x, y ):
        '''Adds new position as head of body and removes last element in body list'''

        newHead = [x,y]
        
        self.body.insert(0, newHead) #inserts new head
        self.body.pop(-1) #removes last element

    def increase_length(self):
        '''Used in conjution with a point increase.
        adds a copy of the last element in body list'''

        self.body.insert(-1, self.body[-1])

    def move(self, keypress):
        '''Executes the the ingame snake logic to for the renderer to use.'''

        self.update_direction(keypress)
        self.move_forward()
        
    def render(self):
        '''renders snake in the passed window object'''

        for part in self.body:
            self.game_window.addstr(part[1], part[0], chr(11035), curses.A_REVERSE)

    def canibal_check(self):
        if self.body[0] in self.body[1:]:
            self.is_alive = False

    def is_contained(self):
        '''Check if snake head is cointaned, returns False if out of bounds'''

        windowHeight, windowWidth = self.game_window.getmaxyx()
        if self.body[0][0] < 1 or self.body[0][0] > windowWidth - 2:
            self.is_alive = False
        if self.body[0][1] < 1 or self.body[0][1] > windowHeight - 2:
            self.is_alive = False
