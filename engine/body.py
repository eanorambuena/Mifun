from eggdriver import Set

from engine.colors import *

origin = [0, 0, 0]

class Triangle(Set):

    def __init__(self, point_1 = origin, point_2 = origin, point_3 = origin, color = blue):
        super().__init__()

        self.addLast(point_1)
        self.addLast(point_2)
        self.addLast(point_3)

        self.color = color

class Body(Set):

    def __init__(self, triangles = [Triangle()]):
        super().__init__()

        for triangle in triangles:
            self.addLast(triangle)

    def draw(self, camera, screen, paint = False):
        transformed_body = Set()

        for triangle in self:

            triangle_verteces = []
            for vertex in triangle:
                r = camera.calculate_position(vertex)
                triangle_verteces.append(r)

            transfromed_triangle = Triangle(triangle_verteces[0], triangle_verteces[1], triangle_verteces[2], color = triangle.color)
            transformed_body.addLast(transfromed_triangle)

        for triangle in transformed_body:
            if paint:
                screen.triangle(triangle[0], triangle[1], triangle[2], color = triangle.color)
            else:
                screen.draw_triangle(triangle[0], triangle[1], triangle[2], color = triangle.color)
    