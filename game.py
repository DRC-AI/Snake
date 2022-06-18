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
        key = self.screen.getch()        
        self.snake.update_direction(key)
        self.snake.move_forward()

        for part in self.snake.body:
            self.screen.addch(part[1], part[0], chr(11035), curses.A_REVERSE)
        
        self.screen.refresh()
        if not self.snake.collision_check():
            exit()

        curses.flushinp()
    
    def render_point(self):
        self.screen.refresh()
        self.screen.addch(self.score.position_y, self.score.position_x, "*")

    def on(self, state):
        while state:
            self.render_point()
            self.render_snake()

            head = self.snake.head
            point = self.score.get_position()

            if head == point:
                self.score.generate_point()
                self.score.increase()
                self.snake.increase_length()
            
            self.screen.clear()
            curses.napms(200)

    #def off(self):
    #   #end game

    #def restart(self):
    #    #restart game

game = Game()
