from ray import * 

r = Raytracer(800, 600)

black = Material(diffuse = color(0, 0, 0))
orange = Material(diffuse = color(255, 140, 0))
white = Material(diffuse = color(255, 255, 255))

r.scene = [
    Sphere(V3(-0.5, -2.2, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0.5, -2.2, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0, -1.8, -16), 0.15, color(255, 140, 0)),
    Sphere(V3(0, -1.4, -16), 0.05, color(0, 0, 0)),
    Sphere(V3(-0.2, -1.45, -16), 0.05, color(0, 0, 0)),
    Sphere(V3(0.2, -1.45, -16), 0.05, color(0, 0, 0)),
    Sphere(V3(-0.4, -1.5, -16), 0.05, color(0, 0, 0)),
    Sphere(V3(0.4, -1.5, -16), 0.05, color(0, 0, 0)),
    Sphere(V3(0, 0, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0, 1, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0, 2, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0, 3, -16), 0.15, color(0, 0, 0)),
    Sphere(V3(0, -2, -16), 1, color(255, 255, 255)),
    Sphere(V3(0, 0.2, -16), 1.5, color(255, 255, 255)),
    Sphere(V3(0, 3, -16), 2, color(255, 255, 255))
]

r.render()
r.write('r.bmp')