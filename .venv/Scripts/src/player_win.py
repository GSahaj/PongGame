import pygame
import pgzero
from Scripts.src.next_level import NextLevel
from pgzero.actor import Actor
import pgzrun

class PlayerOne(NextLevel):
    def __init__(self, width, height, sounds=None):
        super().__init__(width, height, sounds)

        self.player_one_win = Actor('player_one_win')

    def draw_frame(self, screen):
        screen.clear()

        self.player_one_win.draw()


class PlayerTwo(NextLevel):
    def __init__(self, width, height, sounds=None):
        super().__init__(width, height, sounds)

        self.player_two_win = Actor('player_two_win')

    def draw_frame(self, screen):
        screen.clear()

        self.player_two_win.draw()
