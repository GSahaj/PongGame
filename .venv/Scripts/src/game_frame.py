import pygame
import pgzero
from pgzero.actor import Actor
import pgzrun
import pdb
import random
import math
from pgzero.keyboard import keyboard


class GameFrame():
    def __init__(self, width, height, sounds=None):
        self.paddle_speed = 20
        self.WIDTH = width
        self.HEIGHT = height
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.p1_score = 0
        self.p1_live = 15
        self.p2_score = 0
        self.p2_live = 15
        self.point_required = 10
        self.level = 1

        self.sounds = sounds
        self.background_colour = Actor('background_colour', (self.WIDTH / 2, self.HEIGHT / 2))
        self.background = Actor('background', (self.WIDTH / 2, self.HEIGHT / 2))
        self.background_net = Actor('background_net', (self.WIDTH / 2, self.HEIGHT / 2))
        
        self.blue_paddle = Actor('blue_paddle', (0, self.HEIGHT/2))
        self.red_paddle = Actor('red_paddle', (800, self.HEIGHT/2))
        self.blue_paddle.x = 30
        self.red_paddle.x = 770

        self.blue_position = (self.blue_paddle.x, self.blue_paddle.y)
        self.red_position = (self.red_paddle.x, self.red_paddle.y)

    def get_p1_score(self):
        return self.p1_score

    def get_p2_score(self):
        return self.p2_score

    def get_p1_live(self):
        return self.p1_live

    def get_p2_live(self):
        return self.p2_live

    def get_points_required(self):
        return self.point_required

    def get_level(self):
        return self.level

    def set_p1_score(self, score):
        self.p1_score = score

    def set_p2_score(self, score):
        self.p2_score = score

    def set_p1_live(self, live):
        self.p1_live = live

    def set_p2_live(self, live):
        self.p2_live = live

    def set_points_required(self, points):
        self.point_required = points

    def set_level(self, level):
        self.level = level

    def basic_information(self, screen):
        screen.clear()
        self.background_colour.draw()
        self.background.draw()
        self.background_net.draw()

        screen.draw.text(f"Player 1 Live: {self.p1_live}", (0, 0), color="blue", fontsize=25)
        screen.draw.text(f"Player 1 Score: {self.p1_score}", (0, 20), color="blue", fontsize=25)
        screen.draw.text(f"Player 2 Live: {self.p2_live}", (600, 0), color="red", fontsize=25)
        screen.draw.text(f"Player 2 Score: {self.p2_score}", (600, 20), color="red", fontsize=25)

        screen.draw.text(f"Level: {self.level}", (375, 0), color="yellow", fontsize=25)
        screen.draw.text(f"Points Required: {self.point_required}", (325, 20), color="yellow", fontsize=25)
        
        self.red_paddle.draw()
        self.blue_paddle.draw()

    def draw_frame(self, screen):
        self.basic_information(screen)
        
    def update_frame(self):
        self.sounds.background_noise.play(-2)
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
                
        self.controls()
        
    def controls(self):
        if keyboard.up:
            self.red_paddle.y -= self.paddle_speed

            if self.red_paddle.top < 0:
                self.red_paddle.y += self.paddle_speed

        if keyboard.down:
            self.red_paddle.y += self.paddle_speed

            if self.red_paddle.bottom > self.HEIGHT:
                self.red_paddle.y -= self.paddle_speed

        if keyboard.w:
            self.blue_paddle.y -= self.paddle_speed

            if self.blue_paddle.top < 0:
                self.blue_paddle.y += self.paddle_speed

        if keyboard.s:
            self.blue_paddle.y += self.paddle_speed

            if self.blue_paddle.bottom > self.HEIGHT:
                self.blue_paddle.y -= self.paddle_speed