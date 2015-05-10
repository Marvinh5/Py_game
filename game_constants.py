from shared import size
import os

brick_size = size(100, 30)
ball_size  = size(24, 24)
game_size = size(800, 600)
pad_size = size(139, 13)

pad_image = os.path.join("Resources", "pad.png")
ball_image = os.path.join("Resources", "ball.png")
brick_image = os.path.join("Resources", "brick.png")
game_over_screen = os.path.join("Resources", "game_over_screen.png")

game_over_sound = os.path.join("Resources", "game_over.wav")
brick_hit_sound = os.path.join("Resources", "hit_brick.wav")
pad_hit_sound = os.path.join("Resources", "hit_brick.wav")
background_sound = os.path.join("Resources", "background.wav")