import curses
from snake import Snake
from score import Score

class Game():

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.curs_set(0)
        curses.noecho()

        self.screen.nodelay(True)
        self.max_height, self.max_width = self.screen.getmaxyx()
        self.snake = Snake(self.max_height, self.max_width)
        self.score = Score(self.max_height, self.max_width)

    def render_snake(self):
        curses.napms(500)
        self.screen.clear()
        
        key = self.screen.getch()        
        self.snake.update_direction(key)
        self.snake.move_forward()

        for part in self.snake.body:
            self.screen.addch(part[1], part[0], "#")
        
        self.screen.refresh()
        if not self.snake.collision_check(self.snake.head):
            exit()

        curses.flushinp()

    #def on(self):
    #   #game on  

    #def off(self):
    #   #end game

    #def restart(self):
    #    #restart game

if __name__ == "__main__":

    game = Game()
    while True:
        game.render_snake()
        game.screen.getch()