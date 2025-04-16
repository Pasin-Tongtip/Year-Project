from config import Config
import pygame as pg
import random


class Equation:
    def __init__(self):
        self.__font = pg.font.Font(None, 60)
        self.__first_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__second_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.__operator = ['+', '-', '*', '/']
        self.__equal = '= ?'

    def draw_equation(self, screen):
        equation = self.__font.render(f'{random.choice(self.__first_number)}{random.choice(self.__second_number)} '
                                  f'{random.choice(self.__operator)} {random.choice(self.__first_number)}'
                                  f'{random.choice(self.__second_number)} {self.__equal}',
                                  True, Config.get("BLACK"))
        equation_cen = equation.get_rect(center=(Config.get("WIN_SIZE_W") // 2, 30))
        screen.blit(equation, equation_cen)
