from lib import *
from color import *
from math import *
from vector import *
from sphere import *
import random

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.clear()
        self.scene = []
        self.density = 1

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color

    def write(self, filename):
        writeBMP(filename, self.width, self.height, self.framebuffer)

    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                if random.random() < self.density:
                    i = ((2 * (x + 0.5) / self.width ) - 1) * ar * tana
                    j = (1 - (2 * (y + 0.5) / self.height )) * tana

                    direction = V3(i, j, -1).normalize()
                    origin = V3(0, 0, 0)
                    c = self.cast_ray(origin, direction)

                    self.point(x, y, c)

        
    def cast_ray(self, origin, direction):
        for o in self.scene:
            if o.ray_intersect(origin, direction):
                return o.material
        else:
            return self.background_color


r = Raytracer(800, 600)

r.scene = [
    Sphere(V3(-3, -2, -16), 1, color(255, 0, 0)),
    Sphere(V3(-3, 0, -16), 1.5, color(0, 255, 0)),
    Sphere(V3(-3, 6, -16), 2, color(0, 0, 255))
]

r.render()
r.write('r.bmp')