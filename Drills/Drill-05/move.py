from pico2d import *

def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

    pass


running = True

open_canvas()
imgBackGround = load_image("KPU_GROUND.png")
imgHandArrow = load_image("hand_arrow.png")
imgCharacter = load_image("animation_sheet.png")

while running:
    clear_canvas()
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()
