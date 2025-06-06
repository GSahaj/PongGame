import pygame
import pgzero
# from pgzero import music, sounds
import pgzrun
import time
from Scripts.src.start_menu import StartMenu
from Scripts.src.game_frame import GameFrame
from Scripts.src.next_level import NextLevel
from Scripts.src.player_win import PlayerOne, PlayerTwo

WIDTH = 800
HEIGHT = 600

current_level = StartMenu(WIDTH, HEIGHT)
game_start = False
game_over = False

def draw():
    current_level.draw_frame(screen)
def update():
    global current_level, game_over, game_start

    final_p1_live = 0
    final_p1_score = 0
    final_p2_live = 0
    final_p2_score = 0

    if not game_start and keyboard.space:
        current_level = NextLevel(WIDTH, HEIGHT, sounds)
        game_start = True
        return

    if not game_over and game_start:
        current_level.update_frame()
        winner = current_level.player_win()

        if winner == 1:
            current_level = PlayerOne(WIDTH, HEIGHT, sounds, current_level.get_p1_live(), current_level.get_p1_score(), current_level.get_p2_live(),current_level.get_p2_score())
            current_level.sounds.background_noise.stop()
            sounds.game_win.play()
            game_over = True

        elif winner == 2:
            current_level = PlayerTwo(WIDTH, HEIGHT, sounds, current_level.get_p1_live(), current_level.get_p1_score(), current_level.get_p2_live(),current_level.get_p2_score())
            current_level.sounds.background_noise.stop()
            sounds.game_win.play()
            game_over = True

    if game_over and keyboard.r:
        current_level = StartMenu(WIDTH, HEIGHT)
        game_start = False
        game_over = False

pgzrun.go()