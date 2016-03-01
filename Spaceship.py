class Spaceship:
    def __init__(self, p, v):
        self.pos = p
        self.vel = v
        self.lives = 3
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False

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
