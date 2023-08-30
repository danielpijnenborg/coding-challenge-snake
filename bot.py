from random import choice
from typing import List, Tuple
import math

import numpy as np

from ...bot import Bot
from ...constants import Move, MOVE_VALUE_TO_DIRECTION
from ...snake import Snake


def is_on_grid(pos: np.array, grid_size: Tuple[int, int]) -> bool:
    """
    Check if a position is still on the grid
    """
    return 0 <= pos[0] < grid_size[0] and 0 <= pos[1] < grid_size[1]


def collides(pos: np.array, snakes: List[Snake]) -> bool:
    """
    Check if a position is occupied by any of the snakes
    """
    for snake in snakes:
        if snake.collides(pos):
            return True
    return False


def create_grid (self, snake: Snake, other_snakes: List[Snake], candies: List[np.array]):
    grid = [[0 for x in range(self.grid_size[0])] for y in range(self.grid_size[1])]
    for x in range(self.grid_size[0]):
        for y in range(self.grid_size[1]):
            score = 0
            for c in candies:
                score = score + (100 / (1 + math.dist([x, y], c)))
            other_snakes.append(snake)
            if collides ([x,y], other_snakes):
                score = -10
            grid[x][y] = score
            # print("%.1f" % score, end=" ")
        # print (";")
    # print(grid)
    max_move = []
    score = -1;
    for move in MOVE_VALUE_TO_DIRECTION:
        target = snake[0] + MOVE_VALUE_TO_DIRECTION[move]
        if is_on_grid(target, self.grid_size):
            # print (move)
            # print(target)
            # print ("score: %.1f" %  grid[target[0]][target[1]])
            if grid[target[0]][target[1]] > score:
                max_move = move
                score = grid[target[0]][target[1]]
    return max_move


class Explorer(Bot):
    """
    Moves randomly, but makes sure it doesn't collide with other snakes
    """

    @property
    def name(self):
        return 'Explorer'

    @property
    def contributor(self):
        return 'Daniel'

    def determine_next_move(self, snake: Snake, other_snakes: List[Snake], candies: List[np.array]) -> Move:
        return create_grid (self, snake, other_snakes, candies)

