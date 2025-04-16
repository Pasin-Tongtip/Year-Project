from config import Config
import pygame as pg


class GameOver:
    def __init__(self):
        self.__font_game_over = pg.font.Font(None, 50)

    def draw_game_over(self, screen, score):
        text1 = self.__font_game_over.render(f'Game Over!', True, Config.get("BLACK"))
        text2 = self.__font_game_over.render(f'Score: {score}', True, Config.get("BLACK"))
        text3 = self.__font_game_over.render(f'Press SPACE BAR to restart', True, Config.get("BLACK"))

        for i, text in enumerate([text1, text2, text3]):
            text_rect = text.get_rect(center=(
                Config.get("WIN_SIZE_W") // 2, Config.get("WIN_SIZE_H") // 2 + i * 50 - 50))
            screen.blit(text, text_rect)
