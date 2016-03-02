import Vector
try: #import SimpleGUI
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

class Spaceship:
    def __init__(self, p, v):
        self.pos = Vector(p) #position vector
        self.vel = Vector(v) #velocity vector
        self.lives = 3
        self.rotCW = False
        self.rotCCW = False
        self.forward = False
        self.gunLoaded = False
        self.missiles = []

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        global frameWidth, frameHeight, x, y
        j = 0 if self.rotCCW or self.rotCW or self.forward else 1 #decide which image is going to be shown depending on the spaceship's state
        frameWidth = imgSize[0]/2 #2 columns
        frameHeight = imgSize[1] #there's only one row

        x = frameWidth*j+frameWidth/2
        y = frameHeight/2
        canvas.draw_image(img, (x, y), (frameWidth, frameHeight), self.pos.getP(), (frameWidth, frameHeight))


    def hit(self, rock): #check whether or not the spaceship hit the rock
        return not ((rock.pos.x>self.pos.x+imgSize[0]) or (rock.pos.x+rock.size<self.pos.x) or (rock.pos.y>self.pos.y+imgSize[1]) or (rock.pos.y+rock.size<self.pos.y))

    def offset(self, c): #boundaries of the image
        if c == 'l': return self.pos.x-frameWidth/2 #left side
        elif c == 'r': return self.pos.x+frameWidth/2 #right side
        elif c == 'u': return self.pos.y-frameHeight/2 #upper side
        else: return self.pos.y+frameHeight/2 #down side

    def shoot(self): #shoot a missile from the canon's position
        v = self.vel.copy()
        v.add(self.pos.mult(imgSize[1]))
        self.missiles.append(Missile((self.offset('u'), self.offset('u')), v))

class Missile:
    def __init__(self, p, v):
        self.pos = Vector(p)
        self.vel = Vector(v)

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_image(missileImg, (10, 10), (20, 20), self.pos.getP(), (20, 20))

    def hit(self, asteroid): #check whether or not the missile reached a rock
        return not ((asteroid.pos.x>self.pos.x+self.pos.w) or (asteroid.pos.x+asteroid.pos.w<self.pos.x) or (asteroid.pos.y>self.pos.y+self.pos.h) or (asteroid.pos.y+asteroid.pos.h<self.pos.y))

    def offset(self, c):
        if c == 'l': return self.pos.x-10
        elif c == 'r': return self.pos.x+10
        elif c == 'u': return self.pos.y-10
        else: return self.pos.y+10
