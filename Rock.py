import Vector

class Rock:
    def __init__(self, p, v):
        self.pos = Vector(p)
        self.vel = Vector(v)

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        pass

    def hit(self, asteroid):
        pass

    def offset(self, c):
        if c=='l': return self.pos.x#-width of the image
        elif c=='r': return self.pos.x#+width of the image
        elif c=='u': return self.pos.y#-height of the image
        else: return self.pos.y#+height of the image
