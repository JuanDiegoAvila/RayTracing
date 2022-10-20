from ray import *
from material import *
from color import *
from light import *
from plane import * 
from sphere import * 
from envmap import * 
from cube import *
from texture import *

r = Raytracer(1000, 700)
r.light = Light(V3(5, -20, 20), 2, color(255, 255, 255))
r.background_color = color(0, 0, 100)

r.envmap = Envmap('./minecraft.bmp')

rubber = Material(diffuse = color(80, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10)
ivory = Material(diffuse = color(100, 100, 80), albedo=[0.695, 0.305, 0, 0], spec=50)
mirror = Material(diffuse = color(255, 255, 255), albedo=[0, 1, 0.8, 0], spec=1425)
mirror2 = Material(diffuse = color(255, 255, 255), albedo=[0.1, 0.1, 0.1, 0], spec=1425)
glass = Material(diffuse = color(150, 180, 200), albedo=[0, 0.5, 0.1, 0.8], spec=125, refractive_index=1.5)

tGrass = Texture('./grass.bmp')
tDirt = Texture('./lados.bmp')
tDirtD = Texture('./dirt.bmp')

# [x izquierda, x derecha, y abajo, y arriba, z frente, z atras]
grass_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tDirt, tDirt, tDirtD, tGrass, tDirt, tDirt])

r.scene = [
    #Sphere(V3(0, -1.5, -10), 1.5, ivory),
    #Sphere(V3(0, 0, -5), 0.5, glass),
    #Sphere(V3(1, 1, -8), 1.7, ivory),
    #Sphere(V3(-2, 1, -10), 2, mirror),
    #Plane(V3(0, 2.7, -5), 2, 2, mirror),
    Cube(V3(-2.6, -2, -10), 1, grass_block)
]

r.render()
r.write('prueba.bmp')