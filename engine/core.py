from pickle import NONE
import numpy as np
from eggdriver import Image, Vector, clearConsole
from math import cos, sin, acos, pi
from matplotlib.pyplot import imsave

from engine.colors import *

class Screen(Image):

    def __init__(self, height = 224, width = 620, bgcolor = black):
        super().__init__(auto_install=False)

        self.height = height
        self.width = width

        self.bgcolor = bgcolor

        self.fill_room()

    def clear(self):
        clearConsole()

    def fill_room(self):
        self.room = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.bgcolor)
            self.room.append(row)

    def print(self):
        from colr import color # Local import
        from eggdriver.resources.constants import limit, square
        b = self.bias
        for vanillaList in self.matrix:
            line = limit
            for j in vanillaList:
                line += color(square, fore=(self.colour(j, 0), self.colour(j, 1), self.colour(j, 2)), back=(0, 0, 0))
            print(line + limit)
        print()

    def print_room(self):
        self.clear()
        self.loadFromRGB(self.room)
        self.print()
    
    @property
    def mid_width(self):
        return int(self.width / 2)

    @property
    def mid_height(self):
        return int(self.height / 2)

    def draw_point(self, x = 0, y = 0, color = white):
        center_x = self.mid_width
        center_y = self.mid_height

        i = center_y - y
        j = center_x + x

        if i < 0:
            return

        elif i >= self.height:
            return

        if j < 0:
            return

        elif j >= self.width:
            return

        self.room[i][j] = color

    def draw_x_axe(self, color = white):
        
        for x in range(-self.mid_width, self.mid_width):
            self.draw_point(x, 0, color)

    def draw_y_axe(self, color = white):

        for y in range(-self.mid_height, self.mid_height):
            self.draw_point(0, y, color)

    def draw_axes(self, color = white):
        self.draw_x_axe(color)
        self.draw_y_axe(color)
        
    def plot(self, function, x = 0, y = 0, color = red, zoom = 10, x_bounds = None):
        zoomed_x = int(self.width / 2 * zoom)

        if x_bounds != None:
            lower = x_bounds[0]
            upper = x_bounds[1]

        else:
            lower = -1 * zoomed_x
            upper = zoomed_x

        for x_ in range(int(lower), int(upper)):
            self.draw_point(round(x + x_), round(y + (function)(x_ / zoom) * zoom), color)

    def parametric_plot(self, x_function, y_function, x = 0, y = 0, color = red, zoom = 10, t_range = range(100)):

        for t in t_range:
            self.draw_point(round(x + x_function(t / zoom) * zoom), round(y + y_function(t / zoom) * zoom), color)

    def custom_parametric_plot(self, x_function, y_function, v_function, x = 0, y = 0, color = red, zoom = 10, u_range = range(10 ** 4)):
        
        for u in u_range:
            v = v_function(u / zoom)
            self.draw_point(round(x + x_function(u / zoom, v) * zoom), round(y + y_function(u / zoom, v) * zoom), color)

    def polar_plot(self, r_function, x = 0, y = 0, color = red, zoom = 10, theta_range = range(10 ** 4)):
        
        def x_func(theta, r):
            return r * cos(theta)

        def y_func(theta, r):
            return r * sin(theta)

        self.custom_parametric_plot(x_func, y_func, r_function, x, y , color, zoom, theta_range)

    def draw_heart(self, x = 0, y = 0, color = red, zoom = 5):

        def x_func(t):
            return 16 * sin(t)**3

        def y_func(t):
            return 13 * cos(t) - 5  * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)

        self.parametric_plot(x_func, y_func, x, y, color, zoom, range(10 ** 3))

    def draw_flower(self, petals = 4, x = 0, y = 0, color = red, zoom = 50):
        
        if petals == 2:
            
            def r_func(theta):
                return max(0, cos(2 * theta)) ** 0.5

        else:
            n = petals

            if n % 2 == 0:
                n = n / 2
                
                if n % 2 == 1:
                    raise(Exception(f"Is not possible to build a flower with {petals} petals"))

            def r_func(theta):
                return cos(n * theta)

        self.polar_plot(r_func, x, y , color, zoom, range(10 ** 4))

    def paint(self, method, coloring_depth = 100, *args, zoom = 5):
        steps = int(coloring_depth * zoom / 5)

        for t in range(1, steps):
            method(*args, zoom)

    def paint_under(self, function, x = 0, y = 0, color = red, zoom = 10, x_bounds = None, y_bounds = None):
        zoomed_x = min(int(self.mid_width * zoom), self.mid_width)

        if x_bounds != None:
            lower = x_bounds[0]
            upper = x_bounds[1]
        else:
            lower = -1 * zoomed_x
            upper = zoomed_x

        if y_bounds != None:
            lower_y = y_bounds[0]
            upper_y = y_bounds[1]
        else:
            lower_y = -self.mid_height
            upper_y = self.mid_height

        for x_ in range(int(lower), int(upper)):
            for y_value in range(
                    max(-self.mid_height, lower_y),
                    min(round(y + (function)(x_ / zoom) * zoom), upper_y)
                ):
                self.draw_point(round(x + x_), y_value, color)

    def paint_over(self, function, x = 0, y = 0, color = red, zoom = 10, x_bounds = None, y_bounds = None):
        zoomed_x = min(int(self.mid_width * zoom), self.mid_width)

        if x_bounds != None:
            lower = x_bounds[0]
            upper = x_bounds[1]
        else:
            lower = -1 * zoomed_x
            upper = zoomed_x

        if y_bounds != None:
            lower_y = y_bounds[0]
            upper_y = y_bounds[1]
        else:
            lower_y = -self.mid_height
            upper_y = self.mid_height

        for x_ in range(int(lower), int(upper)):
            for y_value in range(
                    max(round(y + (function)(x_ / zoom) * zoom), lower_y),
                    min(self.mid_height, upper_y)
                ):
                self.draw_point(round(x + x_), y_value, color)

    def split_regions(self, function, x = 0, y = 0, colors = [red, red] , zoom = 10, x_bounds = None, y_bounds = None):
        zoomed_x = min(int(self.mid_width * zoom), self.mid_width)

        if x_bounds != None:
            lower = x_bounds[0]
            upper = x_bounds[1]
        else:
            lower = -1 * zoomed_x
            upper = zoomed_x

        if y_bounds != None:
            lower_y = y_bounds[0]
            upper_y = y_bounds[1]
        else:
            lower_y = -self.mid_height
            upper_y = self.mid_height

        for x_ in range(int(lower), int(upper)):
            for y_value in range(-self.mid_height, self.mid_height):
                fy = round(y + (function)(x_ / zoom) * zoom)

                if y_value < max(fy, lower_y):              
                    self.draw_point(round(x + x_), y_value, colors[0])
                elif y_value == fy:
                    self.draw_point(round(x + x_), y_value, colors[1])
                elif y_value > min(fy, upper_y):
                    self.draw_point(round(x + x_), y_value, colors[2])

    def heart(self, x = 0, y = 0, color = red, zoom = 5):
        coloring_depth = 600

        steps = int(coloring_depth * zoom / 5)

        for t in range(1, steps):
            self.draw_heart(x, y, color, zoom * t / steps)

    def flower(self, petals = 4, x = 0, y = 0, color = red, zoom = 5):
        coloring_depth = 100

        steps = int(coloring_depth * zoom / 5)

        for t in range(1, steps):
            self.draw_flower(petals, x, y, color, zoom * t / steps)

    def draw_vertical_line(self, x, y1, y2 = 0, color = violet, zoom = 1):
        lower = min(y1, y2)
        upper = max(y1, y2)

        for y in range(int(zoom * lower), int(zoom * upper)):
            self.draw_point(round(x), round(y), color)

        return

    def draw_line(self, point_1, point_2 = [0, 0], color = violet, zoom = 1):

        x1, y1 = point_1[0], point_1[1]
        x2, y2 = point_2[0], point_2[1]

        if zoom < 0:
            zoom *= -1
            x1, x2, y1, y2 = -x1, -x2, -y1, -y2

        if (x2 - x1) != 0:
            m = (y2 - y1) / (x2 - x1)

            def f(x):
                return y1 + m * (x - x1)

            lower = min(x1, x2)
            upper = max(x1, x2)

            self.plot(f, 0, 0, color, zoom, [zoom * lower, zoom * upper])

        else:
            self.draw_vertical_line(x1, y1, y2, color, zoom)

    def draw_triangle(self, point_1, point_2, point_3 = [0, 0], color = yellow, zoom = 1):
        self.draw_line(point_1, point_2, color, zoom)
        self.draw_line(point_1, point_3, color, zoom)
        self.draw_line(point_3, point_2, color, zoom)

    def draw_vector(self, point, color = yellow, zoom = 1):
        self.draw_line(point, color, zoom)

    def is_point_inside_triangle(self, point, triangule_points):
        point_1 = triangule_points[0]
        point_2 = triangule_points[1]
        point_3 = triangule_points[2]

        A = Vector(point_1)
        B = Vector(point_2)
        C = Vector(point_3)

        _A = A.scale(-1)
        D = B.plus(_A)
        E = C.plus(_A)

        theta = abs(acos(D.dot(E) / (D.dot(D) * E.dot(E))))
        cross = D.dot(D) * E.dot(E) * sin(theta)
        Area = cross / 2

        if E[1] == 0 or (D[0] * E[1] - D[1] * E[0]) == 0:
            Cx = C[0]
            Cy = C[1] + 0.00001
            C = Vector([Cx, Cy])

            _A = A.scale(-1)
            D = B.plus(_A)
            E = C.plus(_A)

        Px = point[0]
        Py = point[1]

        w1 = (E[0] * (A[1] + Py) + E[1] * (Px - A[0])) / (D[0] * E[1] - D[1] * E[0])
        w2 = (Py - A[1] - w1 * D[1]) / E[1]

        return w1 >= 0 and w2 >= 0 and w1 + w2 <= 1

    def triangle(self, point_1, point_2, point_3 = [0, 0], color = yellow, zoom = 1):

        A = Vector(point_1)
        B = Vector(point_2)
        C = Vector(point_3)

        triangle_points = [A.scale(zoom), B.scale(zoom), C.scale(zoom)]

        for y in range(-self.mid_height, self.mid_height):

            for x in range(-self.mid_width, self.mid_width):

                if self.is_point_inside_triangle([x, y], triangle_points):
                    self.draw_point(x, y, color)
    
    @property
    def room_with_tuples(self):
        array = self.room[:]

        for i in range(len(array)):
            for j in range(len(array[0])):
                array[i][j] = tuple(array[i][j])

        return array

    def save(self, file_name = "result.png"):
        array = np.array(self.room_with_tuples, dtype=np.uint8)
        imsave(file_name, array)
