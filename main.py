
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

def update_state(state):
    
    states = {
            1 : play,
            2 : paus,
            3 : terminate
            }
    
    return states[state]()

def play(sceen, snake, menu, score):
    
    key = screen.get_key()
    
    snake.move(key)
    
    if score.is_point(snake.body[0]):
        score.increase_score()
        snake.increase_length()
        score.generate_point()

    if len(snake.length) > 2 :
        snake.canibal_check()

    snake.is_contained()
    snake.render()

    score.render()

    screen.game_window.refresh()
    screen.game_window.erase()
    screen.game_window.border()

def paus():
    pass

def terminate():
    pass

def main(screen):
    
    #Initialization
    screen = Screen()
    screen.initialize_screen()

    snake = Snake(screen.game_window)
    menu = Menu(screen.game_window)
    score = Score(screen.game_window)

    while True:
        
        state = 1

        update_state(state)

wrapper(main) 
