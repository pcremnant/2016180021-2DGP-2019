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

open_canvas(KPU_WIDTH, KPU_HEIGHT)
imgBackGround = load_image("KPU_GROUND.png")
imgCharacter = load_image("animation_sheet.png")

# frame 0 -> left run
# frame 1 -> right run
# frame 2 -> left wait
# frame 3 -> right wait
# 800 x 400

points = [(-300, 200), (400, 350), (300, -300), (-200, -200)]


def draw_curve_points():
    global points

    for j in range(0, 4, 1):
        for i in range(0, 100, 2):
            t = i / 100
            x = ((-t ** 3 + 2 * t ** 2 - t) * points[j % 4][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % 4][
                0] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % 4][0] + (t ** 3 - t ** 2) *
                 points[(j + 3) % 4][0]) / 2
            y = ((-t ** 3 + 2 * t ** 2 - t) * points[j % 4][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j + 1) % 4][
                1] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j + 2) % 4][1] + (t ** 3 - t ** 2) * points[(j + 3) % 4][
                     1]) / 2
            draw_point((x, y))
        draw_point(points[(j + 2) % 4])

while running:
    clear_canvas()
    # imgBackGround.draw(100, 100)

    imgBackGround.clip_draw(0, 0, KPU_WIDTH, KPU_HEIGHT,
                            KPU_WIDTH / 2, KPU_HEIGHT / 2, 1280, 1024)

    update_canvas()
    handle_events()
    nFrame = (nFrame + 1) % 8

    delay(0.01)

close_canvas()
