from config import Config
import pygame as pg


class HealthBar:
    def __init__(self):
        self.__position = (10, 10)

    def draw(self, screen):
        x, y = self.__position
        rect = pg.Rect(x * Config.get('GRID_SIZE'),
                       y * Config.get('WIN_SIZE_W') / 8,
                       Config.get('GRID_SIZE'),
                       Config.get('GRID_SIZE'))
        pg.draw.rect(screen, Config.get('BLACK'), rect)
