class Intersect:
    def __init__(self, distance, point, normal, norm_coord = None, face = None):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.norm_coord = norm_coord
        self.face = face