
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
from screen import *

'''Checklista
    * Skapa play funktion som itererar genom gameloopen
    * Skapa paus funktion som stoppar spel logiken
    * Skapa terminate funktion som stänger spelet
    '''



def main(screen):
    
wrapper(main) 
