from random import choice
from typing import List, Tuple
import math

import numpy as np

from ...bot import Bot
from ...constants import Move, MOVE_VALUE_TO_DIRECTION
from ...snake import Snake

np.set_printoptions(precision=1)

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
    x = np.arange(self.grid_size[0])
    y = self.grid_size[1]-1 - np.arange(self.grid_size[1])
    nx = np.ones(self.grid_size[0])
    ny = np.ones(self.grid_size[1])
    xg = np.outer(ny, x)
    yg = np.outer(y, nx)
    scoregrid = np.zeros(self.grid_size)
    for c in candies:
        scoregrid = scoregrid + (100 / (1 +(xg-c[0])**2+(yg-c[1])**2))
    other_snakes.append(snake)
    for snake in other_snakes:
        print (snake)
        for p in snake.positions:
            scoregrid[self.grid_size[1]-1-p[1]][p[0]] = -10
    # print (scoregrid)
    max_move = []
    score = -9;
    for move in MOVE_VALUE_TO_DIRECTION:
        target = snake[0] + MOVE_VALUE_TO_DIRECTION[move]
        if is_on_grid(target, self.grid_size):
            # print (move)
            # print(target)
            # print ("score: %.1f" %  scoregrid[self.grid_size[1]-1-target[1]][target[0]])
            if scoregrid[self.grid_size[1]-1-target[1]][target[0]] > score:
                max_move = move
                score = scoregrid[self.grid_size[1]-1-target[1]][target[0]]
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

