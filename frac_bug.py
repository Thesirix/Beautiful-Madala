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

