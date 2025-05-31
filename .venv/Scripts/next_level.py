import pygame
import pgzero
from pgzero.actor import Actor
import pgzrun
import random
import math
from Scripts.game_frame import GameFrame


class NextLevel(GameFrame):
    def __init__(self, width, height, sounds=None):
        super().__init__(width, height, sounds)

        self.TABLE_LEFT = 0
        self.TABLE_RIGHT = 800
        self.TABLE_TOP = 100
        self.TABLE_BOTTOM = 500

        self.default_position = (self.WIDTH/2, self.HEIGHT/2)
        self.ping_pong = Actor('pongball', self.default_position)
        self.ping_pong_speed = 5
        self.ball_paused = False
        self.pause_end_time = 0

        self.movement_calculation()


    def get_ping_pong_speed(self):
        return self.ping_pong_speed

    def set_ping_pong_speed(self, speed):
        self.ping_pong_speed = speed

    def draw_frame(self, screen):
        super().draw_frame(screen)
        self.ping_pong.draw()

    def draw_frame(self, screen):
        super().draw_frame(screen)
        self.ping_pong.draw()

    def update_frame(self):
        super().update_frame()
        self.move_ball()

    def movement_calculation(self):
        m1_dx = random.uniform(-1, 1)
        m1_dy = random.uniform(-1, 1)

        magnitude = math.sqrt(m1_dx ** 2 + m1_dy ** 2)

        self.m1_dx = (m1_dx / magnitude) * self.ping_pong_speed
        self.m1_dy = (m1_dy / magnitude) * self.ping_pong_speed

    def move_ball(self):
        if self.ball_paused:
            if pygame.time.get_ticks() >= self.pause_end_time:
                self.ball_paused = False
            return

        self.ping_pong.x += self.m1_dx
        self.ping_pong.y += self.m1_dy
        
        if self.ping_pong.y < self.TABLE_TOP or self.ping_pong.y > self.TABLE_BOTTOM:
            self.m1_dy *= -1

        self.paddle_collision()
        self.missed_shot()
        self.level_up()

    def paddle_collision(self):
        current_time = pygame.time.get_ticks()

        if self.ping_pong.colliderect(self.blue_paddle) and not self.invulnerable and self.m1_dx < 0:
             self.set_p1_score(self.get_p1_score() + 1)
             self.m1_dx *= -1
             self.invulnerable = True
             self.last_collision_time = current_time
             self.movement_calculation()

        elif self.ping_pong.colliderect(self.red_paddle) and not self.invulnerable and self.m1_dx > 0:
            self.set_p2_score(self.get_p2_score() + 1)
            self.m1_dx *= -1
            self.invulnerable = True
            self.last_collision_time = current_time
            self.movement_calculation()

        if self.m1_dx > 0:
            self.ping_pong.x += 5

        else:
            self.ping_pong.x -= 5

    def missed_shot(self):
        if not self.ball_paused:
            if self.ping_pong.x < self.TABLE_LEFT:
                self.set_p1_live(self.get_p1_live() - 1)
                self.sounds.lose_point.play()
                self.ping_pong.pos = self.default_position
                self.ball_paused = True
                self.pause_end_time = pygame.time.get_ticks() + 1000

            if self.ping_pong.x > self.TABLE_RIGHT:
                self.set_p2_live(self.get_p2_live() - 1)
                self.sounds.lose_point.play()
                self.ping_pong.pos = self.default_position
                self.ball_paused = True
                self.pause_end_time = pygame.time.get_ticks() + 1000

    def level_up(self):
        if self.get_p1_score() + self.get_p2_score() == self.get_points_required():
            if not self.get_level() == 4:
                self.set_level(self.get_level() + 1)
                self.set_points_required(self.get_points_required() + math.floor(self.get_points_required() * 1.5))
                self.set_ping_pong_speed(self.get_ping_pong_speed() + 2)

    def player_win(self):
        if self.get_p1_live() == 0:
            return 2

        if self.get_p2_live() == 0:
            return 1

        if self.get_p1_score() == 100:
            return 1

        if self.get_p2_score() == 100:
            return 2

        if self.get_level() == 4 and self.get_p1_score() + self.get_p2_score() > self.get_points_required():
            if self.get_p1_score() > self.get_p2_score():
                return 1
            else:
                return 2

        return None
