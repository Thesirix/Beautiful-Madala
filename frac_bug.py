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

def on_right_click(x, y):
    turtle.clear()

def draw_while_mouse_down(x, y):
    global drawing, last_pos
    if drawing:
        distance = math.sqrt((x - last_pos[0])**2 + (y - last_pos[1])**2)
        if distance > threshold:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            num_petals, color = generate_mandala_params()
            draw_mandala(num_petals, color)
            last_pos = (x, y)

def close_program(event):
    global running
    running = False
    turtle.getcanvas().unbind('<Destroy>')  
    turtle.bye()

def on_close():
    global closing
    if not closing:
        close_program(None)

turtle.speed(0)
turtle.tracer(0)

turtle.getcanvas().bind("<Button-1>", lambda event: on_button_down(event.x - turtle.window_width() / 2, turtle.window_height() / 2 - event.y))
turtle.getcanvas().bind("<ButtonRelease-1>", lambda event: on_button_up(event.x - turtle.window_width() / 2, turtle.window_height() / 2 - event.y))
turtle.getcanvas().bind("<Button-3>", lambda event: on_right_click(event.x - turtle.window_width() / 2, turtle.window_height() / 2 - event.y))
turtle.getcanvas().bind("<Motion>", lambda event: draw_while_mouse_down(event.x - turtle.window_width() / 2, turtle.window_height() / 2 - event.y))

turtle.getcanvas().bind("<Destroy>", close_program)
turtle.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)  
turtle.mainloop()