from plane import *
from vector import *

class Cube(object):
    def __init__(self, center, w, material, texture = []):
        self.center = center
        self.w = w
        self.material = material
        self.texture = texture

    def ray_intersect(self, origin, direction):

        min = V3(round((self.center.x - self.w/2), 2), round((self.center.y - self.w/2), 2), round((self.center.z - self.w/2), 2))
        max = V3(round((self.center.x + self.w/2), 2), round((self.center.y + self.w/2), 2), round((self.center.z + self.w/2), 2))
        
        tmin = 9999999
        tmax = 9999999

        if direction.x != 0:
            tmin = ((self.center.x - self.w/2) - origin.x) / direction.x
            tmax = ((self.center.x + self.w/2) - origin.x) / direction.x


        if tmin > tmax:
            tmin, tmax = tmax, tmin
        
        tymin = ((self.center.y - self.w/2) - origin.y) / direction.y
        tymax = ((self.center.y + self.w/2) - origin.y) / direction.y

        if tymin > tymax:
            tymin, tymax = tymax, tymin
        
        if tmin > tymax or tymin > tmax:
            return False
        
        if tymin > tmin:
            tmin = tymin
        
        if tymax < tmax:
            tmax = tymax

        tzmin = ((self.center.z - self.w/2) - origin.z) / direction.z
        tzmax = ((self.center.z + self.w/2) - origin.z) / direction.z

        if tzmin > tzmax:
            tzmin, tzmax = tzmax, tzmin
        
        if tmin > tzmax or tzmin > tmax:
            return False
        
        if tzmin > tmin:
            tmin = tzmin
        
        if tzmax < tmax:
            tmax = tzmax
        
        if tmin > tmax:
            return False

        normal = V3(0, 0, 0)
        impact = origin + (direction * tmin)
        impact = V3(round(impact.x, 2), round(impact.y, 2), round(impact.z, 2))

        face = None
        # [x izquierda, x derecha, y abajo, y arriba, z frente, z atras] se asignan indices

        if impact.x >= min.x and impact.y >= min.y and impact.z == min.z:
            normal = V3(0, 0, -1)
            face = 5
        
        elif impact.x >= min.x and impact.y >= min.y and impact.z == max.z:
            normal = V3(0, 0, 1)
            face = 4

        elif impact.x >= min.x and impact.y == min.y and impact.z >= min.z:
            normal = V3(0, 1, 0)
            face = 2

        elif impact.x >= min.x and impact.y == max.y and impact.z >= min.z:
            normal = V3(0, -1, 0)
            face = 3
        
        elif impact.x == min.x and impact.y >= min.y and impact.z >= min.z:
            normal = V3(-1, 0, 0)
            face = 0
        
        elif impact.x == max.x and impact.y >= min.y and impact.z >= min.z:
            normal = V3(1, 0, 0)
            face = 1

        if normal == V3(0, 0, 0):
            return False

        if tmin < 0:
            return False

        x, y = self.getNormal(face, impact)

        return Intersect(
            distance = tmin,
            point = impact,
            normal = normal,
            norm_coord = V3(x, y, 0),
            face = face
        )

    def getNormal(self, face, impact):
        if face == 0:
            minH = (self.center.z - self.w/2)
            minV = (self.center.y - self.w/2)

            z = (impact.z - minH) / self.w
            y = (impact.y - minV) / self.w

            return z, y
        
        elif face == 1:
            minH = (self.center.z + self.w/2)
            minV = (self.center.y - self.w/2)

            z = (impact.z - minH) / self.w
            y = (impact.y - minV) / self.w

            return z, y

        elif face == 2:
            minH = (self.center.x - self.w/2)
            minV = (self.center.z - self.w/2)

            x = (impact.x - minH) / self.w
            z = (impact.z - minV) / self.w

            return x, z
        
        elif face == 3:

            minH = (self.center.x - self.w/2)
            minV = (self.center.z + self.w/2)

            x = (impact.x - minH) / self.w
            z = (impact.z - minV) / self.w

            return x, z

        elif face == 4:
            minH = (self.center.x - self.w/2)
            minV = (self.center.y - self.w/2)

            x = (impact.x - minH) / self.w
            y = (impact.y - minV) / self.w

            return x, y

        elif face == 5:
            minH = (self.center.x + self.w/2)
            minV = (self.center.y - self.w/2)

            x = (impact.x - minH) / self.w
            y = (impact.y - minV) / self.w

            return x, y







