from config import Config
from score import Score
from snake import Snake
from food import Food
from game_over import GameOver
from equation import Equation
from health_bar import HealthBar
import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode((Config.get('WIN_SIZE_W'), Config.get('WIN_SIZE_H')))
        self.__screen.fill(Config.get('WHITE'))
        self.__clock = pg.time.Clock()
        self.__running = True
        self.__snake = Snake()
        self.__food = Food()
        self.__game_reset()
        self.__score = Score()
        self.__game_over_ui = GameOver()
        self.__equation = Equation()
        self.__health_bar = HealthBar()
        self.__dict_keys = {pg.K_UP: 'UP',
                            pg.K_DOWN: 'DOWN',
                            pg.K_LEFT: 'LEFT',
                            pg.K_RIGHT: 'RIGHT'}

    def __game_reset(self):
        self.__game_over = False
        self.__food.randomize()
        self.__snake.reset()

    def __user_event(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                self.__running = False
            elif ev.type == pg.KEYDOWN:
                if self.__game_over:
                    if ev.key == pg.K_SPACE:
                        self.__game_reset()
                else:
                    if ev.key in self.__dict_keys:
                        self.__snake.set_direction(self.__dict_keys[ev.key])

    def __screen_update(self):
        self.__screen.fill(Config.get('WHITE'))
        if (not self.__game_over) and (not self.__snake.move()):
            self.__game_over = True

        if (self.__snake.get_snake_head()[0] == self.__food.get_position()[0] and
                self.__snake.get_snake_head()[1] == self.__food.get_position()[1]):
            self.__snake.increase_length()
            self.__food.randomize()

        self.__snake.draw(self.__screen)
        self.__food.draw(self.__screen)
        self.__score.draw_score(self.__screen, self.__snake.get_snake_length() - 1)
        self.__equation.draw_equation(self.__screen)
        # self.__health_bar.draw(self.__screen)

        if self.__game_over:
            self.__screen.fill(Config.get('LIGHT_GREY'))
            self.__game_over_ui.draw_game_over(self.__screen, self.__snake.get_snake_length() - 1)

        self.__clock.tick(10)
        pg.display.update()

    def game_loop(self):
        while self.__running:
            self.__user_event()
            self.__screen_update()


if __name__ == '__main__':
    g1 = Game()
    g1.game_loop()
