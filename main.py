import time
import curses
from curses import wrapper
from snake import *
from score import *
from game import *

def main(screen):
    while True:
        game.on()
wrapper(main) 
