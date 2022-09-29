class color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    

    def __mul__(self, other):
        if(type(other) == int or type(other) == float):
            r = self.r * other
            g = self.g * other
            b = self.b * other
        else:
            r = self.r * other.r
            g = self.g * other.g
            b = self.b * other.b

        return color(self.clamping(r), self.clamping(g), self.clamping(b))

    def toBytes(self):
        return bytes([self.b, self.g, self.r])

    def color_range(self, r, g, b):
        return color(self.clamping(r*255), self.clamping(g*255), self.clamping(b*255))

    def clamping(self, num):
        return int(max(min(num, 255), 0))

