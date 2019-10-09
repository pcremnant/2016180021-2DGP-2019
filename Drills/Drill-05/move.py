from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

nFrameMode = 3
nFrame = 0
nMouseX = 0
nMouseY = 0
nCharacterX = 100
nCharacterY = 100


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
        # elif event.type == SDL_MOUSEBUTTONDOWN:
    # if event.key

    pass


running = True

open_canvas()
imgBackGround = load_image("KPU_GROUND.png")
imgHandArrow = load_image("hand_arrow.png")
imgCharacter = load_image("animation_sheet.png")

# frame 0 -> left run
# frame 1 -> right run
# frame 2 -> left wait
# frame 3 -> right wait
# 800 x 400

while running:
    clear_canvas()
    # imgBackGround.draw(100, 100)
    imgBackGround.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT,
                            KPU_WIDTH / 2, KPU_HEIGHT / 2, 1280, 1024)

    imgHandArrow.draw(nMouseX + 17, 600 - nMouseY - 23)
    imgCharacter.clip_draw(nFrame * 100, nFrameMode * 100,
                           100, 100, nCharacterX, nCharacterY)
    update_canvas()
    handle_events()
    nFrame = (nFrame + 1) % 8

    delay(0.01)

close_canvas()
