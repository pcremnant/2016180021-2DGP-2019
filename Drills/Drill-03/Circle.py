import math
from pico2d import *

cx=400
cy=300
r=200
angle = 0.0

open_canvas(800,600)


grass = load_image('grass.png')
character = load_image('character.png')

while(angle<100):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(r*math.cos(angle)+cx,r*math.sin(angle)+cy)
    angle = angle+0.1
    delay(0.1)

close_canvas()
