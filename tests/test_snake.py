import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
    
    def test_reverse(self):
        self.assertEqual(self.snake.reverse(curses.KEY_DOWN), curses.KEY_DOWN)