import curses
from enum import Enum

class States(Enum):
    ON = 1 
    OFF = 2
    RESTART = 3

class Menu():
    def __init__(self, window):

        self.selector = 0 #indicates wich button is selected
    
    def run_action(self, action):
        
        menuActions = {
                "Try Again" : game.on,
                "Exit" : exit()
                }

        menuActions[action]()

    def display_menu(self):

        y, x = self.window.getmaxyx()

        middle_y = y // 2
        middle_x = x // 2

        for i in self.menuItems:
            if self.selector == self.menuItems.index(i):
                self.window.addstr( middle_y + self.menuItems.index(i), middle_x - (len(i) // 2), i, curses.A_REVERSE)
            else:
                self.window.addstr( middle_y + self.menuItems.index(i), middle_x - (len(i) // 2), i)

    def update_selector(self, keypress):
        
        if keypress == curses.KEY_UP:
            self.selector = self.selector - 1
            if self.selector < 0 :
                self.selector = 0

        elif keypress == curses.KEY_DOWN:
            self.selector = self.selector + 1
            if self.selector > len(self.menuItems) - 1:
                self.selector = len(self.menuItems) - 1

    def render(self, keypress):

        if keypress == 10:
            return self.run_action()
        self.update_selector(keypress)
        self.display_menu()