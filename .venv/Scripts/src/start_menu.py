import pygame
import pgzero
from Scripts.src.next_level import NextLevel
from pgzero.actor import Actor
import pgzrun

class StartMenu():
    def __init__(self, width, height):

        self.start_screen = Actor('start_screen')

    def draw_frame(self, screen):
        screen.clear()
        self.start_screen.draw()

    def update_frame(self):
        pass