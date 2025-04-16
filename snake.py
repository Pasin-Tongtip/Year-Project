from config import Config
import pygame as pg
import random


class Snake:
    def __init__(self):
        self.__dirs = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
        self.__positions = []
        self.reset()

    def reset(self):
        self.__positions = []
        center_grid = [Config.get('GRID_COUNT_W') // 2, Config.get('GRID_COUNT_H') // 2]
        self.__positions.append(center_grid)
        self.__length = 1
        self.__direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def get_snake_length(self):
        return self.__length

    def get_snake_head(self):
        return self.__positions[0]

    def increase_length(self):
        self.__length += 1
        print(self.__length)
        print(self.__positions)

    def move(self):
        tmp_dir = (self.__positions[0][0] + self.__dirs[self.__direction][0],
                   self.__positions[0][1] + self.__dirs[self.__direction][1])

        if (tmp_dir[0] < 0 or tmp_dir[0] >= Config.get('GRID_COUNT_W')
                or tmp_dir[1] < 0 or tmp_dir[1] >= Config.get('GRID_COUNT_H')
                or self.__positions[0] in self.__positions[1:]):
            return False

        self.__positions.insert(0, tmp_dir)

        while len(self.__positions) > self.__length:
            self.__positions.pop()

        return True

    def set_direction(self, direction):
        self.__direction = direction

    def draw(self, screen):
        for pos in self.__positions:
            x, y = pos
            rect = pg.Rect(x * Config.get('GRID_SIZE') + 1,
                           y * Config.get('GRID_SIZE') + 1,
                           Config.get('GRID_SIZE') - 2,
                           Config.get('GRID_SIZE') - 2)
            pg.draw.rect(screen, Config.get('BLACK'), rect)
