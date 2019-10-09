from pico2d import *

nFrameMode = 0
nMouseX = 0
nMouseY = 0

def handle_events():
    global running
    global nFrameMode
    global nMouseX
    global nMouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
             nMouseX = event.x
             nMouseY = event.y
        #elif event.type == SDL_MOUSEBUTTONDOWN:
# if event.key

    pass


running = True

open_canvas()
imgBackGround = load_image("KPU_GROUND.png")
imgHandArrow = load_image("hand_arrow.png")
imgCharacter = load_image("animation_sheet.png")

while running:
    clear_canvas()
    imgHandArrow.draw(nMouseX + 17, 600 - nMouseY - 23)
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()
