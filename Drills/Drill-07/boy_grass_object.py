from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x > 700:
            pass
        else:
            self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self, t):
        self.x, self.y = random.randint(100, 700), 599
        self.type = t
        if t % 2 == 0:
            self.image = load_image("ball21x21.png")
        else:
            self.image = load_image("ball41x41.png")
        self.speed = random.randint(3, 7)

    def update(self):
        if self.y >= 50:
            self.y -= self.speed
        elif self.y < 50:
            pass

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    global boys
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
boys = [Boy() for i in range(11)]
balls = [Ball(random.randint(1, 2)) for i in range(20)]

grass = Grass()
running = True
# game main loop code
while running:
    handle_events()

    for boy in boys:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in boys:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)
close_canvas()

# finalization code
