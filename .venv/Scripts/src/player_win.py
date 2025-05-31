import pygame
import pgzero
from Scripts.src.next_level import NextLevel
from pgzero.actor import Actor
import pgzrun

class PlayerOne(NextLevel):
    def __init__(self, width, height, sounds=None, p1_live=0, p1_score=0, p2_live=0, p2_score=0):
        super().__init__(width, height, sounds)
        self.set_p1_live(p1_live)
        self.set_p1_score(p1_score)
        self.set_p2_live(p2_live)
        self.set_p2_score(p2_score)
        self.player_one_win = Actor('player_one_win')

    def draw_frame(self, screen):
        screen.clear()
        self.player_one_win.draw()
        screen.draw.text(f"Player 1 Live: {self.get_p1_live()}", (300, 400), color="blue", fontsize=40)
        screen.draw.text(f"Player 1 Score: {self.get_p1_score()}", (300, 430), color="blue", fontsize=40)
        screen.draw.text(f"Player 2 Live: {self.get_p2_live()}", (300, 500), color="red", fontsize=40)
        screen.draw.text(f"Player 2 Score: {self.get_p2_score()}", (300, 530), color="red", fontsize=40)

class PlayerTwo(NextLevel):
    def __init__(self, width, height, sounds=None, p1_live=0, p1_score=0, p2_live=0, p2_score=0):
        super().__init__(width, height, sounds)
        self.set_p1_live(p1_live)
        self.set_p1_score(p1_score)
        self.set_p2_live(p2_live)
        self.set_p2_score(p2_score)
        self.player_two_win = Actor('player_two_win')

    def draw_frame(self, screen):
        screen.clear()
        self.player_two_win.draw()
        screen.draw.text(f"Player 1 Live: {self.get_p1_live()}", (300, 400), color="blue", fontsize=40)
        screen.draw.text(f"Player 1 Score: {self.get_p1_score()}", (300, 430), color="blue", fontsize=40)
        screen.draw.text(f"Player 2 Live: {self.get_p2_live()}", (300, 500), color="red", fontsize=40)
        screen.draw.text(f"Player 2 Score: {self.get_p2_score()}", (300, 530), color="red", fontsize=40)
