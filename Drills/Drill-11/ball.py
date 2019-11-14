import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), 60, 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0
    # fill here for def stop


# fill here
class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class BlockBar:
    image = None
    DIRECTION_LEFT = -1
    DIRECTION_RIGHT = 1

    def __init__(self):
        if BlockBar.image is None:
            image = load_image('brick180x40.png')
        self.x, self.y = 0, 200
        self.direction = BlockBar.DIRECTION_RIGHT

    def get_bb