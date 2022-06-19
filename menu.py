import curses

class Menu():
    def __init__(self, max_height, max_width, game):

        self.game = game
        self.max_height = max_height
        self.max_width = max_width
        self.selector = 0

        self.items = ["restart" ,
                      "leaderboard",
                      "exit"]
    
    def run_action(self):
        
        menuActions = {
                "restart" : self.game.restart,
                "leaderboard" : exit,
                "exit" : exit
                }

        action = self.items[self.selector]
        menuActions[action]()

    def update_selector(self, keypress):
        
        if keypress == curses.KEY_UP:
            self.selector = self.selector - 1
            if self.selector < 0 :
                self.selector = 0

        elif keypress == curses.KEY_DOWN:
            self.selector = self.selector + 1
            if self.selector > len(self.items) - 1:
                self.selector = len(self.items) - 1