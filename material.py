
class Material(object):
    def __init__(self, diffuse, albedo, spec, refractive_index = 0, texture = None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = texture
    
    def changeDiffuse(self, intersect):
        textura = self.texture[intersect.face]
        nuevo = textura.getColor(intersect.norm_coord.x, intersect.norm_coord.y)
        self.diffuse = nuevo
