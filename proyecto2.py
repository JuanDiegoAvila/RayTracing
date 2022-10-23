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
r.light = Light(V3(0, -20, 20), 2, color(255, 255, 255))
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
tNetherrack = Texture('./Textures/netherrack.bmp')
tMagma = Texture('./Textures/magma.bmp')

# [x izquierda, x derecha, y abajo, y arriba, z frente, z atras]
grass_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tDirt, tDirt, tDirtD, tGrass, tDirt, tDirt])
wood_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tWood, tWood, tWoodTop, tWoodTop, tWood, tWood])
leaves_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tLeaves, tLeaves, tLeaves, tLeaves, tLeaves, tLeaves])
wood_plank_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tPlank, tPlank, tPlank, tPlank, tPlank, tPlank])
obsidian_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tObsidian, tObsidian, tObsidian, tObsidian, tObsidian, tObsidian])
portal_block = Material(diffuse = color(138, 43, 226), albedo=[0.9, 0.8, 0.3, 0], spec=125, refractive_index=1.9, texture = [tPortal, tPortal, tPortal, tPortal, tPortal, tPortal])
netherrack_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tNetherrack, tNetherrack, tNetherrack, tNetherrack, tNetherrack, tNetherrack])
magma_block = Material(diffuse = color(0, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, texture = [tMagma, tMagma, tMagma, tMagma, tMagma, tMagma])

r.scene = [
    Cube(V3(-2.5, -2, -14), 1, grass_block),
    Cube(V3(-1.5, -2, -14), 1, netherrack_block),
    Cube(V3(-0.5, -2, -14), 1, magma_block),
    Cube(V3(0.5, -2, -14), 1, netherrack_block),
    Cube(V3(1.5, -2, -14), 1, netherrack_block),
    Cube(V3(2.5, -2, -14), 1, netherrack_block),
    Cube(V3(3.5, -2, -14), 1, netherrack_block),
    Cube(V3(4.5, -2, -14), 1, grass_block),
    Cube(V3(5.5, -2, -14), 1, grass_block),
    Cube(V3(6.5, -2, -14), 1, grass_block), # primera fila
    Cube(V3(-4.5, -2, -15), 1, grass_block),
    Cube(V3(-3.5, -2, -15), 1, grass_block),
    Cube(V3(-2.5, -2, -15), 1, netherrack_block),
    Cube(V3(-1.5, -2, -15), 1, netherrack_block),
    Cube(V3(-0.5, -2, -15), 1, netherrack_block),
    Cube(V3(0.5, -2, -15), 1, netherrack_block),
    Cube(V3(1.5, -2, -15), 1, netherrack_block),
    Cube(V3(2.5, -2, -15), 1, netherrack_block),
    Cube(V3(3.5, -2, -15), 1, netherrack_block),
    Cube(V3(4.5, -2, -15), 1, grass_block),
    Cube(V3(5.5, -2, -15), 1, grass_block),
    Cube(V3(6.5, -2, -15), 1, grass_block), # segunda fila
    Cube(V3(-5.5, -2, -16), 1, grass_block),
    #Cube(V3(-6.5, -2, -16), 1, grass_block),
    Cube(V3(-5.5, -2, -16), 1, grass_block),
    Cube(V3(-4.5, -2, -16), 1, netherrack_block),
    Cube(V3(-3.5, -2, -16), 1, netherrack_block),
    Cube(V3(-2.5, -2, -16), 1, netherrack_block),
    Cube(V3(-1.5, -2, -16), 1, netherrack_block),
    Cube(V3(-1.5, -1, -16), 1, magma_block),
    Cube(V3(-2.5, -1, -16), 1, netherrack_block),
    Cube(V3(-2.5, 0, -16), 1, netherrack_block),
    Cube(V3(-3.5, -1, -16), 1, magma_block),
    Cube(V3(-1.5, 0, -16), 1, netherrack_block),
    Cube(V3(-1.5, 1, -16), 1, netherrack_block),
    Cube(V3(-0.5, -1, -16), 1, obsidian_block),
    Cube(V3(-0.5, 0, -16), 1, obsidian_block),
    Cube(V3(0.5, 0, -16), 1, portal_block),
    Cube(V3(1.5, 0, -16), 1, portal_block),
    Cube(V3(-0.5, 1, -16), 1, obsidian_block),
    Cube(V3(0.5, 1, -16), 1, portal_block),
    Cube(V3(1.5, 1, -16), 1, portal_block),
    Cube(V3(-0.5, 2, -16), 1, obsidian_block),
    Cube(V3(0.5, 2, -16), 1, portal_block),
    Cube(V3(1.5, 2, -16), 1, portal_block),
    Cube(V3(-0.5, 3, -16), 1, obsidian_block),
    Cube(V3(0.5, 3, -16), 1, obsidian_block),
    Cube(V3(1.5, 3, -16), 1, obsidian_block),
    Cube(V3(2.5, 3, -16), 1, obsidian_block),
    Cube(V3(2.5, 0, -16), 1, obsidian_block),
    Cube(V3(2.5, 1, -16), 1, obsidian_block),
    Cube(V3(2.5, 2, -16), 1, obsidian_block),
    Cube(V3(2.5, 3, -16), 1, obsidian_block),
    Cube(V3(0.5, -1, -16), 1, obsidian_block),
    Cube(V3(1.5, -1, -16), 1, obsidian_block),
    Cube(V3(2.5, -1, -16), 1, obsidian_block),
    Cube(V3(3.5, 2, -16), 1, netherrack_block),
    Cube(V3(3.5, 1, -16), 1, netherrack_block),
    Cube(V3(3.5, 0, -16), 1, netherrack_block),
    Cube(V3(4.5, 0, -16), 1, magma_block),
    Cube(V3(4.5, 1, -16), 1, netherrack_block),
    Cube(V3(5.5, 0, -16), 1, netherrack_block),
    Cube(V3(3.5, -1, -15), 1, magma_block),
    Cube(V3(4.5, -1, -15), 1, netherrack_block),
    Cube(V3(5.5, -1, -15), 1, netherrack_block), # estructura y portal
    Cube(V3(-7.5, -2, -15), 1, wood_block),
    Cube(V3(-7.5, -1, -15), 1, wood_block),
    Cube(V3(-7.5, 0, -15), 1, wood_block),
    Cube(V3(-7.5, 3, -14), 1, leaves_block),
    Cube(V3(-8.5, 3, -15), 1, leaves_block),
    Cube(V3(-6.5, 3, -15), 1, leaves_block),
    Cube(V3(-7.5, 3, -16), 1, leaves_block),
    Cube(V3(-7.5, 4, -14), 1, leaves_block),
    Cube(V3(-8.5, 4, -15), 1, leaves_block),
    Cube(V3(-6.5, 4, -15), 1, leaves_block),
    Cube(V3(-7.5, 4, -16), 1, leaves_block),
    Cube(V3(-7.5, 1, -14), 1, leaves_block),
    Cube(V3(-7.5, 1, -13), 1, leaves_block),
    Cube(V3(-6.5, 2, -13), 1, leaves_block),
    Cube(V3(-5.5, 2, -13), 1, leaves_block),
    Cube(V3(-5.5, 2, -14), 1, leaves_block),
    Cube(V3(-5.5, 2, -15), 1, leaves_block),
    Cube(V3(-5.5, 2, -16), 1, leaves_block),
    Cube(V3(-5.5, 2, -17), 1, leaves_block),
    Cube(V3(-5.5, 1, -17), 1, leaves_block),
    Cube(V3(-5.5, 1, -16), 1, leaves_block),
    Cube(V3(-7.5, 2, -13), 1, leaves_block),
    Cube(V3(-6.5, 1, -14), 1, leaves_block),
    Cube(V3(-6.5, 1, -13), 1, leaves_block),
    Cube(V3(-5.5, 1, -14), 1, leaves_block),
    Cube(V3(-8.5, 1, -13), 1, leaves_block),
    Cube(V3(-8.5, 1, -15), 1, leaves_block),
    Cube(V3(-9.5, 1, -15), 1, leaves_block),
    Cube(V3(-7.5, 1, -13), 1, leaves_block),
    Cube(V3(-8.5, 2, -13), 1, leaves_block),
    Cube(V3(-7.5, 1, -16), 1, leaves_block),
    Cube(V3(-7.5, 1, -17), 1, leaves_block),
    Cube(V3(-6.5, 1, -15), 1, leaves_block),
    Cube(V3(-5.5, 1, -15), 1, leaves_block),
]



r.render()
r.write('Proyecto2.bmp')