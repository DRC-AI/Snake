
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

def initializeSettings( stdscr ):

    #Setup
    curses.noecho()
    curses.curs_set(0)

    h,w = stdscr.getmaxyx()

    snake_window = stdscr.subwin( h-2,w-2,1,1 )

    snake = Snake(snake_window)


    snake_window.border()
    snake_window.nodelay(True)
    snake_window.keypad(True)

    score = Score(snake_window)
    score.generate_point()

    menu = curseMenu(snake_window)

    return (snake_window, snake, score, menu)


def gameOn(snake_window, snake, score, menu):

        while snake.isAlive:
            keypress = snake_window.getch()
            snake.move(keypress) #Updates direction and moves the snake one step.
        
            if score.is_point(snake.body[0]): #Checks if snake Head and point overlap
                score.increase_score() 
                snake.increaseBodyLength()
                score.generate_point()

            if len(snake.body) > 2 : 

                snake.canibalCheck() #Checks if snake eats itself

            snake.isContained() #Checks if snake is within bounds

            snake.render()
            score.render(snake_window)

            snake_window.refresh()
            snake_window.erase()
            snake_window.border()
            snake_window.addstr( 1, 2 ,"Your score:" + " " + str(score.score))
            curses.flushinp() #Flushes input so it doesnt add upp while curses "naps".
            curses.napms(100) #Makes the loop "nap", decrease to make snake move faster.


def main(stdscr):
    
    stdscr = curses.initscr() #Initializes the main curses window

    h, w = stdscr.getmaxyx() #Used to adjust the game size based on the size of terminal window

    snake_window, snake, score, menu = initializeSettings(stdscr) 

    runGame = True
    
    #Game loop
    while runGame:

        gameOn(snake_window, snake, score, menu) #the Main game loop

        while True: #Executes when main game loop exits

            gameOverMessage = "Game Over"
            scoreMessage = "Your Score: " + str(score.score)
            stdscr.addstr( (h // 2) - 3,(w // 2) - (len(gameOverMessage) // 2), gameOverMessage) 
            stdscr.addstr( (h // 2) - 2,(w // 2) - (len(scoreMessage) // 2), scoreMessage) 
            snake.isAlive = menu.render(snake_window.getch()) #Restores isAlive variable if player wants to restart.
            
            if snake.isAlive:
                
                snake_window, snake, score, menu = initializeSettings(stdscr) #Resets everything

                gameOn(snake_window, snake, score, menu) #Runs the main loop in case snake is alive again.
   
wrapper(main) 
