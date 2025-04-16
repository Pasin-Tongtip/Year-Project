from config import Config
import pygame as pg
import random


class Food:
    def __int__(self):
        self.randomize()

    def randomize(self):
        self.__position = (random.randint(0, Config.get('GRID_COUNT_W') - 1),
                           random.randint(0, Config.get('GRID_COUNT_H') - 1))

    def draw(self, screen):
        x, y = self.__position
        rect = pg.Rect(x * Config.get('GRID_SIZE'),
                       y * Config.get('GRID_SIZE'),
                       Config.get('GRID_SIZE'),
                       Config.get('GRID_SIZE'))
        pg.draw.rect(screen, Config.get('RED'), rect)

    def get_position(self):
        return self.__position
