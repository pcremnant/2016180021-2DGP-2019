from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

nFrameMode = 3
nFrame = 0

bArrived = False
bSetPoint = False


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    # if event.key

    pass


running = True

open_canvas(KPU_WIDTH, 600)
imgBackGround = load_image("KPU_GROUND.png")
imgCharacter = load_image("animation_sheet.png")

# frame 0 -> left run
# frame 1 -> right run
# frame 2 -> left wait
# frame 3 -> right wait
# 800 x 400

pointNumber = 10
points = [(0, 500), (600, 600), (600, 0), (100, 100)]


def draw_curve_player():
    global points
    global nFrameMode
    global nFrame

    for j in range(0, pointNumber, 1):
        for i in range(0, 100, 2):
            t = i / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * points[j % pointNumber][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % pointNumber][
                0] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % pointNumber][0] + (t ** 3 - t ** 2) *
                 points[(j + 3) % pointNumber][0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * points[j % pointNumber][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % pointNumber][
                1] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % pointNumber][1] + (t ** 3 - t ** 2) * points[(j + 3) % pointNumber][
                     1]) / 2

            if points[(j+1) % pointNumber][0] < points[(j+2) % pointNumber][0]:
                nFrameMode = 0
            else :
                nFrameMode = 1
            clear_canvas()
            imgBackGround.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT,
                                    KPU_WIDTH / 2, KPU_HEIGHT / 2, 1280, 1024)
            imgCharacter.clip_draw(nFrame * 100, nFrameMode * 100, 100, 100, x, y)
            update_canvas()
            handle_events()
            nFrame = (nFrame + 1) % 8
            delay(0.01)


while running:
    clear_canvas()
    # imgBackGround.draw(100, 100)

    imgBackGround.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT,
                            KPU_WIDTH / 2, KPU_HEIGHT / 2, 1280, 1024)
    update_canvas()
    draw_curve_player()

    delay(0.01)

close_canvas()
