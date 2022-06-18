import unittest
import curses
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake( 79,79)
        self.snake.direction = curses.KEY_DOWN
    
    def test_reversed_up(self):
        self.assertEqual(self.snake.reversed(curses.KEY_UP), True)

    def test_reversed_down(self):
        self.assertEqual(self.snake.reversed(curses.KEY_DOWN), False)
    
    def test_valid_key(self):
        self.assertEqual(self.snake.valid_key(curses.KEY_DOWN), True)
        self.assertEqual(self.snake.valid_key(curses.KEY_UP), True)
        self.assertEqual(self.snake.valid_key(curses.KEY_LEFT), True)
        self.assertEqual(self.snake.valid_key(curses.KEY_RIGHT), True)
        self.assertEqual(self.snake.valid_key(curses.KEY_MAX), False)
    
    def test_update_direction(self):
        self.assertEqual(self.snake.update_direction(curses.KEY_UP), curses.KEY_DOWN)
        self.assertEqual(self.snake.update_direction(curses.KEY_LEFT), curses.KEY_LEFT)
        self.assertEqual(self.snake.update_direction(curses.KEY_RIGHT), curses.KEY_LEFT)
    
    def test_move_forward(self):
        self.assertEqual(self.snake.move_forward(), self.snake.body)
        self.assertEqual(len(self.snake.move_forward()), len(self.snake.body))
    
    def test_collision_check(self):
        self.assertEqual(self.snake.collision_check(79,79), False) 
        self.assertNotEqual(self.snake.collision_check(79,79), True) 
        self.assertEqual(self.snake.collision_check(80,79), True) 
        self.assertEqual(self.snake.collision_check(100,100), True) 
        self.assertEqual(self.snake.collision_check(-79,-79), True) 
    
    def test_increase_length(self):
        self.assertEqual(len(self.snake.increase_length()), 3)

if __name__ == "__main__":
    unittest.main()