import random
from pico2d import *
import game_world
import game_framework


class Ball:
    def __init__(self):
        self.x = random.randint(100, 900)
        self.y = random.randint(50, 700)
        self.is_delete = False
        pass

    def draw(self):
        pass

    def get_bb(self):
        pass

    def update(self):
        pass


class BigBall(Ball):
    image = None

    def __init__(self):
        super().__init__()
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.width = 41
        self.height = 41
        self.hp = 100
        self.type = 'big'

    def draw(self):
        draw_rectangle(*self.get_bb())
        BigBall.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.width // 2, self.y - self.height // 2, self.x + self.width // 2, self.y + self.height // 2


class SmallBall(Ball):
    image = None

    def __init__(self):
        super().__init__()
        if SmallBall.image is None:
            SmallBall.image = load_image('ball21x21.png')
        self.width = 21
        self.height = 21
        self.hp = 50
        self.type = 'small'

    def draw(self):
        draw_rectangle(*self.get_bb())

        SmallBall.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.width // 2, self.y - self.height // 2, self.x + self.width // 2, self.y + self.height // 2

# ------------------------------------------
