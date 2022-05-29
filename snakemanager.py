import curses 

class snake():

    def __init__(self, gameWindow):
        '''Sets default settings to snake object'''

        self.positiony, self.positionx = gameWindow.getmaxyx()

        #centers the position of snake to middle of passed window
        self.positiony = self.positiony // 2
        self.positionx = self.positionx // 2 

        #initializes the snake body list using its position properties
        self.body = [ [self.positionx, self.positiony], [self.positionx - 1, self.positiony  ] ]
        #initializes direction
        self.direction = ""

        #initializes isAlive property to True
        self.isAlive = True

        #initializes gameWindow property to passed window
        self.gameWindow = gameWindow

    def checkIfBackwards(self, keypress) :
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

    def updateDirection(self, keypress):
        '''Used to update direction of head.
        Needs keypress in curse.KEY_DIRECTION format.'''

        #Only updates if key i valid
        validKeys = [ curses.KEY_LEFT,curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN ]
        
        if self.checkIfBackwards(keypress):

            if keypress not in validKeys:
                return self.direction
            else :
                self.direction = keypress
                return self.direction
        else:
            return self.direction

    def moveForward(self):
        '''Makes the snake move forward 1 step in the facing direction
        and updates the body list'''
        
        if self.direction == curses.KEY_LEFT:
            self.positionx = self.positionx - 1
        elif self.direction == curses.KEY_RIGHT:
            self.positionx = self.positionx + 1
        elif self.direction == curses.KEY_UP:
            self.positiony = self.positiony - 1
        elif self.direction == curses.KEY_DOWN:
            self.positiony = self.positiony + 1

        self.updateBodyPos(self.positionx, self.positiony)

    def updateBodyPos(self, x, y ):
        '''Adds new position as head of body and removes last element in body list'''

        newHead = [x,y]
        
        self.body.insert( 0, newHead ) #inserts new head
        self.body.pop(-1) #removes last element

    def increaseBodyLength(self):
        '''Used in conjution with a point increase.
        adds a copy of the last element in body list'''

        self.body.insert(-1, self.body[-1])

    def move(self, keypress):
        '''Executes the the ingame snake logic to for the renderer to use.'''

        self.updateDirection(keypress)
        self.moveForward()
        
    def render(self):
        '''renders snake in the passed window object'''

        for part in self.body:
            self.gameWindow.addstr(part[1], part[0], chr(11035), curses.A_REVERSE)

    def canibalCheck(self):
        if self.body[0] in self.body[1:]:
            self.isAlive = False

    def isContained(self):
        '''Check if snake head is cointaned, returns False if out of bounds'''

        windowHeight, windowWidth = self.gameWindow.getmaxyx()
        if self.body[0][0] < 1 or self.body[0][0] > windowWidth - 2:
            self.isAlive = False
        if self.body[0][1] < 1 or self.body[0][1] > windowHeight - 2:
            self.isAlive = False
