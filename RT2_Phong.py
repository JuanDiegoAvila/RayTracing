from ray import *
from color import *

r = Raytracer(800, 600)
r.light = Light(V3(-3, 0, 0), 1, color(255, 255, 255))
r.background_color = color(234, 221, 202)
rubber = Material(diffuse = color(218, 160, 109), albedo=[0.9, 0.1], spec=10)
rubber_red = Material(diffuse = color(100, 0, 0), albedo=[0.9, 0.4], spec=10)
rubber_dark = Material(diffuse = color(123, 63, 0), albedo=[0.9, 0.4], spec=10)
#ivory = Material(diffuse = color(100, 100, 80), albedo=[0.6, 0.3], spec=50)
black_glass = Material(diffuse = color(0, 0, 0), albedo=[0.895, 0.8], spec=50)

r.scene = [
    Sphere(V3(0, 0, -16), 2, rubber_red), # estomago 
    Sphere(V3(-2.1, -1.3, -14), 0.9, rubber), # pata izquierda arriba
    Sphere(V3(2.1, -1.3, -14), 0.9, rubber), # pata derecha arriba
    Sphere(V3(-1.8, 1.7, -14), 0.9, rubber), # pata izquierda abajo
    Sphere(V3(1.8, 1.7, -14), 0.9, rubber), # pata derecha abajo
    Sphere(V3(0, -2.9, -14), 1.5, rubber), # cabeza 
    Sphere(V3(-1.4, -3.9, -14), 0.7, rubber_dark), # oreja izquierda
    Sphere(V3(1.4, -3.9, -14), 0.7, rubber_dark), # oreja derecha
    Sphere(V3(0, -2.6, -13), 0.7, rubber_dark), # boca
    Sphere(V3(0, -2.6, -12), 0.2, black_glass), # nariz
    Sphere(V3(-0.5, -3, -12), 0.09, black_glass), # ojo izquierdo
    Sphere(V3(0.5, -3, -12), 0.09, black_glass), # ojo derecho
]

r.render()
r.write('RT2.bmp')