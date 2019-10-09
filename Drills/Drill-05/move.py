from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

nFrameMode = 3
nFrame = 0
nMouseX = 0
nMouseY = 0
nCharacterX = 100
nCharacterY = 100
nArriveX = 100
nArriveY = 100

bArrived = False
bSetPoint = False


def handle_events():
    global running
    global nFrameMode
    global nMouseX
    global nMouseY
    global nArriveX
    global nArriveY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            nMouseX = event.x + 17
            nMouseY = 600 - event.y - 23
        elif event.type == SDL_MOUSEBUTTONDOWN:
            nArriveX = event.x + 17
            nArriveY = 600 - event.y - 23
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

i = 0
t = i / 100

p1 = (nCharacterX, nCharacterY)
p2 = (nArriveX, nArriveY)

while running:
    clear_canvas()
    # imgBackGround.draw(100, 100)

    imgBackGround.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT,
                            KPU_WIDTH / 2, KPU_HEIGHT / 2, 1280, 1024)

    imgHandArrow.draw(nMouseX, nMouseY)
    if bArrived:
        imgCharacter.clip_draw(nFrame * 100, nFrameMode * 100,
                               100, 100, nCharacterX, nCharacterY)

    if nCharacterX == nArriveX and nCharacterY == nArriveY:
        bArrived = True
    else:
        bArrived = False

    if bArrived:
        if nFrameMode == 0:
            nFrameMode = 2
        elif nFrameMode == 1:
            nFrameMode = 3
    elif not bSetPoint:
        bSetPoint = True
        p1 = (nCharacterX, nCharacterY)
        p2 = (nArriveX, nArriveY)
    elif bSetPoint:
        if i < 100:
            i = i + 1
            t = i / 100
            x = (1 - t) * p1[0] + t * p2[0]
            y = (1 - t) * p1[1] + t * p2[1]
            imgCharacter.clip_draw(nFrame * 100, nFrameMode * 100,
                                   100, 100, x, y)
        elif i == 100 or t == 1:
            nCharacterX = nArriveX
            nCharacterY = nArriveY
            i = 0
            t = 0
            bArrived = True
            bSetPoint = False
    update_canvas()
    handle_events()
    nFrame = (nFrame + 1) % 8

    delay(0.01)

close_canvas()
