import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

img = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/double_ship.png")
missileImg = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/shot3.png")
imgSize = (180, 90)
imgCentre = (90, 45)
frameWidth = imgSize[0]/2 #2 columns
frameHeight = imgSize[1] #there's only one row
x = frameWidth/2
y = frameHeight/2
canvasSize = (600, 400)

class Spaceship:
    def __init__(self, p, v):
        self.pos = Vector(p)
        self.vel = Vector(v)
        self.lives = 3
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        global frameWidth, frameHeight, x, y
        j = 0 if self.moveUp or self.moveDown or self.moveLeft or self.moveRight else 1
        frameWidth = imgSize[0]/2 #2 columns
        frameHeight = imgSize[1] #there's only one row

        x = frameWidth*j+frameWidth/2
        y = frameHeight/2
        canvas.draw_image(img, (x, y), (frameWidth, frameHeight), self.pos.getP(), (frameWidth, frameHeight))


    def hit(self, asteroid):
        pass

    def offset(self, c):
        if c == 'l': return self.pos.x-frameWidth/2
        elif c == 'r': return self.pos.x+frameWidth/2
        elif c == 'u': return self.pos.y-frameHeight/2
        else: return self.pos.y+frameHeight/2


class Missile:
    def __init__(self, p, v):
        self.pos = p
        self.vel = v

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_image(missileImg, (10, 10), (20, 20), self.pos.getP(), (20, 20))

    def hit(self, asteroid):
        return not ((asteroid.pos.x>self.pos.x+self.pos.w) or (asteroid.pos.x+asteroid.pos.w<self.pos.x) or (asteroid.pos.y>self.pos.y+self.pos.h) or (asteroid.pos.y+asteroid.pos.h<self.pos.y))

    def offset(self, c):
        if c == 'l': return self.pos.x-10
        elif c == 'r': return self.pos.x+10
        elif c == 'u': return self.pos.y-10
        else: return self.pos.y+10
