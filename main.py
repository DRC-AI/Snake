import time
import curses
from curses import wrapper
from snake import *
from score import *
from menu import *
from game import *

def main(screen):
   game.on(True) 
wrapper(main) 
