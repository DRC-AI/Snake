import curses

class Screen():

    def __init__(self):
        self.screen = curses.initscr()
        self.screen_height, self.screen_width = self.screen.getmaxyx()
        self.game_window = self.screen.subwin(self.screen_height-1, self.screen_width-1, 1, 1)
    
    def initialize_screen():
        curses.noecho()
        curses.curs_set(0)
        self.game_window.border()
        self.game_window.nodelay(True)
        self.game_window.keypad(True)

