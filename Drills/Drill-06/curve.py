import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     ' + str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_curve_points():
    global points

    draw_big_point(points[0])
    draw_big_point(points[1])
    draw_big_point(points[2])
    draw_big_point(points[3])

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


points = [(-300, 200), (400, 350), (300, -300), (-200, -200)]

prepare_turtle_canvas()
while True:
    draw_curve_points()
# draw_curve_4_points(points[0], points[1], points[2], points[3])
turtle.done()
