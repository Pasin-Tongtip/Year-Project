from config import Config
import pygame as pg


class Score:
    def __init__(self):
        self.__font = pg.font.Font(None, 36)

    def draw_score(self, screen, score):
        score_text = self.__font.render(f'Score: {score}', True, Config.get("BLACK"))
        screen.blit(score_text, (675, 30))
