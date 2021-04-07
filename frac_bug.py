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

