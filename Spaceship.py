try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

img = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/double_ship.png")
imgSize = (180, 90)
imgCentre = (90, 45)
frameWidth = imgSize[0]/2 #2 columns
frameHeight = imgSize[1] #there's only one row
x = frameWidth/2
y = frameHeight/2
canvasSize = (600, 400)

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
        global frameWidth, frameHeight, x, y
        j = 0 if self.moveUp or self.moveDown or self.moveLeft or self.moveRight else 1
        frameWidth = imgSize[0]/2 #2 columns
        frameHeight = imgSize[1] #there's only one row

        x = frameWidth*j+frameWidth/2
        y = frameHeight/2
        canvas.draw_image(img, (x, y), (frameWidth, frameHeight), (canvasSize[0]/2, canvasSize[1]/2), (frameWidth, frameHeight))


    def hit(self, asteroid):
        pass

    def offset(self, c):
        if c == 'l': return self.pos.x#-width of the image
        elif c == 'r': return self.pos.x#+width of the image
        elif c == 'u': return self.pos.y#-height of the image
        else: return self.pos.y#+height of the image


class Missile:
    def __init__(self, p, v):
        self.pos = p
        self.vel = v

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        pass

    def hit(self, asteroid):
        pass

    def offset(self, c):
        if c == 'l':
            return self.pos.x  # -width of the image
        elif c == 'r':
            return self.pos.x  # +width of the image
        elif c == 'u':
            return self.pos.y  # -height of the image
        else:
            return self.pos.y  # +height of the image
