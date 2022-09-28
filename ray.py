from lib import *
from color import *
from math import *
from vector import *
from sphere import *
from material import *
from light import * 
import random

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.scene = []
        self.density = 1
        self.light = None
        self.clear()


    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c.toBytes() or self.current_color.toBytes()

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
        material, intersect = self.scene_intersect(origin, direction)
        
        if material is None:
            return self.background_color

        light_direction = (self.light.position - intersect.point).normalize()
        intensity = light_direction @ intersect.normal

        return material.diffuse * intensity
            
    
    
    def scene_intersect(self, origin, direction):
        zbuffer = 999999
        material = None
        intersect = None

        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect

        return material, intersect

r = Raytracer(800, 600)
r.light = Light(V3(-3, 0, 0), 1)

red = Material(diffuse = color(255, 0, 0))
white = Material(diffuse = color(255, 255, 255))

r.scene = [
    Sphere(V3(-3, 0, -16), 2, red),
    Sphere(V3(2.8, 0, -10), 2, white)
]

r.render()
r.write('r.bmp')