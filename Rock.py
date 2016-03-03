import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

img = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/asteroid_blue.png")

class Rock:
    def __init__(self, p, v):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.size = 90

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_image(img, (self.size/2, self.size/2), (self.size, self.size), self.pos.getP(), (self.size, self.size))

    def offset(self, c):
        if c == 'l': return self.pos.x-self.size/2
        elif c == 'r': return self.pos.x+self.size/2
        elif c == 'u': return self.pos.y-self.size/2
        else: return self.pos.y+-self.size/2
