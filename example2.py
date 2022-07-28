from    engine import *

SCREEN_WIDTH = 4320
SCREEN_HEIGHT = 1440
BGCOLOR = black

engine_screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, BGCOLOR)

def setup(screen):
    screen.draw_axes()

    a = 0.1
    b = 9

    Weistrass = I * 0
    for n in range(100):
        Weistrass =  Weistrass + Cos[X * (b ** n * pi)] * (a ** n)

    screen.split_regions(Weistrass, colors = [red, violet, blue], zoom = 150)
    screen.paint_over(Sqrt[X ** 2 * -1 + I * 2500] + 300, color = yellow, x_bounds = [-49, 49], y_bounds = [250, 350])

def loop(screen):
    screen.draw_axes()

setup(engine_screen)
engine_screen.save()
