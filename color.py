class color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    

    def __mul__(self, other):
        r = self.r
        g = self.g
        b = self.b

        if(type(other) == int or type(other) == float):
            r *= other
            g *= other
            b *= other
        else:
            r *= other.r
            g *= other.g
            b *= other.b

        return color(self.clamping(r), self.clamping(g), self.clamping(b))

    def __add__(self, other):
        r = self.r
        g = self.g
        b = self.b

        if(type(other) == int or type(other) == float):
            r += other
            g += other
            b += other
        else:
            r += other.r
            g += other.g
            b += other.b

        return color(self.clamping(r), self.clamping(g), self.clamping(b))

    def toBytes(self):
        return bytes([self.b, self.g, self.r])

    def color_range(self, r, g, b):
        return color(self.clamping(r*255), self.clamping(g*255), self.clamping(b*255))

    def clamping(self, num):
        return int(max(min(num, 255), 0))

