import curses
from snake import Snake
from score import Score
from menu import Menu

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
        self.menu = Menu(self.max_height, self.max_width, self)

    def render_snake(self):
        
        key = self.screen.getch()       
        self.snake.update_direction(key)
        self.snake.move_forward()

        for part in self.snake.body:
            try:
                self.screen.addch(part[1], part[0], chr(11035), curses.A_REVERSE)
            except:
                continue
        
    def render_point(self):
        
        self.screen.refresh()
        self.screen.addch(self.score.position_y, self.score.position_x, "*")
    
    def render_score(self):
        
        score_message = "Score: " + str(self.score.score)
        self.screen.addstr(0,0, score_message)
        self.screen.refresh()

    def render_menu(self):

        middle_y = self.max_height // 2
        middle_x = self.max_width // 2

        for i in self.menu.items:
            try:
                if self.menu.selector == self.menu.items.index(i):
                    self.screen.addstr( middle_y + self.menu.items.index(i), middle_x - (len(i) // 2), i.capitalize(), curses.A_REVERSE)
                else:
                    self.screen.addstr( middle_y + self.menu.items.index(i), middle_x - (len(i) // 2), i.capitalize())
            except:
                continue
        
        key = self.screen.getch()
        self.menu.update_selector(key)
        
        if key == 10: #enter
            self.menu.run_action()

    def on(self):

        while self.snake.is_alive:
            self.render_score()
            self.render_point()
            self.render_snake()

            head = self.snake.head
            point = self.score.get_position()

            if head == point:
                self.score.generate_point()
                self.score.increase()
                self.snake.increase_length()
            
            if self.snake.canbibal():
                while True:
                    self.render_menu()

            self.screen.refresh() 
            self.screen.clear()
            curses.flushinp()
            curses.napms(100)
    
    def restart(self):
        self.snake = Snake(self.max_height, self.max_width)
        self.score = Score(self.max_height, self.max_width)
        self.on()


game = Game()