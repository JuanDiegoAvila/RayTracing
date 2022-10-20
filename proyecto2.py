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

tGrass = Texture('./Textures/grass.bmp')
tDirt = Texture('./Textures/lados.bmp')
tDirtD = Texture('./Textures/dirt.bmp')
tWood = Texture('./Textures/wood.bmp')
tWoodTop = Texture('./Textures/wood_top.bmp')
tLeaves = Texture('./Textures/leaves.bmp')
tPlank = Texture('./Textures/plank.bmp')
tObsidian = Texture('./Textures/obsidian.bmp')
tPortal = Texture('./Textures/portal.bmp')

# [x izquierda, x derecha, y abajo, y arriba, z frente, z atras]
grass_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tDirt, tDirt, tDirtD, tGrass, tDirt, tDirt])
wood_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tWood, tWood, tWoodTop, tWoodTop, tWood, tWood])
leaves_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tLeaves, tLeaves, tLeaves, tLeaves, tLeaves, tLeaves])
wood_plank_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tPlank, tPlank, tPlank, tPlank, tPlank, tPlank])
obsidian_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tObsidian, tObsidian, tObsidian, tObsidian, tObsidian, tObsidian])
portal_block = Material(diffuse = color(138, 43, 226), albedo=[0.9, 0.8, 0.3, 0], spec=125, refractive_index=1.9, texture = [tPortal, tPortal, tPortal, tPortal, tPortal, tPortal])

r.scene = [
    Cube(V3(-2.5, -2, -10), 1, grass_block),
    Cube(V3(-1.5, -2, -10), 1, wood_block),
    Cube(V3(-0.5, -2, -10), 1, leaves_block),
    Cube(V3(0.5, -2, -10), 1, wood_plank_block),
    Cube(V3(1.5, -2, -10), 1, obsidian_block),
    Cube(V3(2.5, -2, -10), 1, portal_block)
]

r.render()
r.write('Proyecto2.bmp')