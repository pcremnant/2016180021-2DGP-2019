import game_framework
import main_state
from pico2d import *

name = "PauseState"
image = None

timer = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            # if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            #     game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    global timer

    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if timer < 0.5:
        image.draw(400, 300)
    delay(0.01)
    timer = timer + 0.01
    if timer > 1.0:
        timer = 0
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
