
''' Hello, welcome to the Snake game by Oskar Lundmark!
    I wrote this game as a learning experience,
    i know there are much to be improved but it
    all works and has all the funtionality
    i set out to create. 

    Maybe in the future i will come back and impove
    the readability and funtionality,
    but really now i just want to hop on
    the next learning experience.
    Thank you for playing my first ever game!'''

import time
import curses
from curses import wrapper
from snake import *
from score import *
from menu import *

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

def main(screen):
    
    #Initialization
    screen = Screen()
    snake = Snake(screen.game_window)
    menu = Menu(screen.game_window)
    score = Score(screen.game_window)
    
wrapper(main) 
