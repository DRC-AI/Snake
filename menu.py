import curses

class curseMenu():
    def __init__(self, window):

        self.menuItems = [ "Try Again", "Exit" ]

        self.window = window
        self.selector = 0 #indicates wich button is selected
    
    def runAction(self):
        '''Runs associated action for menu item'''
        
        menuActions = {
                "Try Again" : self.tryAgain,
                "Exit" : self.exit
                }
        game = menuActions[self.menuItems[self.selector]]()
        return game

    def tryAgain(self):
        game = True
        return game

    def exit(self):
        quit()

    def displayMenu(self):
        '''Displays menu in provided window'''

        y, x  = self.window.getmaxyx()
            
        middle_y = y // 2
        middle_x = x // 2

        for i in self.menuItems:
            if self.selector == self.menuItems.index(i):
                self.window.addstr( middle_y + self.menuItems.index(i), middle_x - (len(i) // 2), i, curses.A_REVERSE)
            else:
                self.window.addstr( middle_y + self.menuItems.index(i), middle_x - (len(i) // 2), i)

    def updateSelector(self, keypress):
        '''updates selector'''
        
        if keypress == curses.KEY_UP:
            self.selector = self.selector - 1
            if self.selector < 0 :
                self.selector = 0

        elif keypress == curses.KEY_DOWN:
                self.selector = self.selector + 1
                if self.selector > len(self.menuItems) - 1:
                    self.selector = len(self.menuItems) - 1

    def render(self, keypress):
        '''Renders menu and handler input inside passed window object'''
        if keypress == 10:
            return self.runAction()
        self.updateSelector(keypress)
        self.displayMenu()

