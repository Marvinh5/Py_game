from shared import size
import os

brick_size = size(100, 30)
ball_size  = size(24, 24)
game_size = size(800, 600)
pad_size = size(139, 13)

pad_image = os.path.join("Resources", "pad.png")
ball_image = os.path.join("Resources", "ball.png")
brick_image = os.path.join("Resources", "brick.png")