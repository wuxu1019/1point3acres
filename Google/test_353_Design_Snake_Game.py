"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)

"""


class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = collections.deque()
        self.snake.append((0, 0))
        self.food = food
        self.p = 0
        self.score = 0
        self.width, self.height = width, height
        self.mp = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        dr, dc = self.mp[direction]

        r, c = self.snake[0]
        n_r, n_c = r + dr, c + dc
        if 0 <= n_r < self.height and 0 <= n_c < self.width:
            self.snake.appendleft((n_r, n_c))
            if self.p < len(self.food) and [n_r, n_c] != self.food[self.p] or self.p >= len(self.food):
                self.snake.pop()
            else:
                self.score += 1
                self.p += 1
            if self.snake.count((n_r, n_c)) > 1:
                return -1
            return self.score
        return -1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)