import curses

class Menu:
    def __init__(self, max_height, max_width, game):

        self.game = game
        self.max_height = max_height
        self.max_width = max_width
        self.selector = 0

        self.items = ["restart" ,
                      "exit"]
    
    def run_action(self):
        
        menu_actions = {
                "restart" : self.game.restart,
                "exit" : exit
                }

        action = self.items[self.selector]
        menu_actions[action]()

    def update_selector(self, key):
        
        if key == curses.KEY_UP:
            self.selector = self.selector - 1
            if self.selector < 0 :
                self.selector = 0

        elif key == curses.KEY_DOWN:
            self.selector = self.selector + 1
            if self.selector > len(self.items) - 1:
                self.selector = len(self.items) - 1