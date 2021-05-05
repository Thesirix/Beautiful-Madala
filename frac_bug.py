import turtle
import random
import math

drawing = False
running = True
last_pos = (0, 0)
threshold = 100
closing = False  


def generate_mandala_params():
    num_petals = random.randint(8, 24) * 2
    color = (random.random(), random.random(), random.random())
    return num_petals, color

def random_fractal(length, order, angle, depth):
    if order == 0 or depth >= 10:
        turtle.forward(length)
    else:
        turtle.left(angle)
        random_fractal(length / 1.5, order - 1, angle, depth + 1)
        turtle.right(angle * 2)
        random_fractal(length / 1.5, order - 1, angle, depth + 1)
        turtle.left(angle)

def draw_fractal_petal(length, order, angle):
    random_fractal(length, order, angle, 0)
    turtle.right(120)
    random_fractal(length, order, angle, 0)
    turtle.right(120)
    random_fractal(length, order, angle, 0)
    turtle.right(120)

def draw_mandala(num_petals, color):
    turtle.pencolor(color)
    angle = 360 / num_petals
    order = 2
    length = 50

    fractal_angle = random.randint(15, 45)

    for _ in range(num_petals):
        draw_fractal_petal(length, order, fractal_angle)
        turtle.right(180 - angle)

def on_button_down(x, y):
    global drawing
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    drawing = True
    num_petals, color = generate_mandala_params()
    draw_mandala(num_petals, color)

def on_button_up(x, y):
    global drawing
    drawing = False

