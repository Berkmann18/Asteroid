#Main class

import Rock
import Spaceship
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

canvasSize = (600, 400)

class Interaction:
    def __init__(self, spaceship, rocks):
        self.spaceship = spaceship
        self.rocks = rocks

    def draw(self, canvas):
        self.spaceship.draw(canvas)
        for r in self.rocks: r.draw(canvas)

    def update(self):
        for r in self.rocks:
            if self.spaceship.hit(r): self.spaceship.lives -= 1 #take a life off the spaceship
        if self.spaceship.lives <= 0: #start over
            game.welcomeScreen["enabled"] = True
            self.rocks = [] #remove all rocks

        if self.spaceship.rotCW: #clockwise rotation of the spaceship
            pass
        if self.spaceship.rotCCW: #counter clockwise rotation of the spaceship
            pass
        if self.spaceship.forward: #go forward
            self.spaceship.update()
        if self.spaceship.gunLoaded: #shoot a missile
            self.spaceship.shoot()
            if self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x > canvasSize[0] or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x < 0 or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y > canvasSize[1] or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y < 0:
                self.spaceship.missiles.pop() #remove the missile that went off-screen


def rect(canvas, a, b, border, borderClr, bgClr): #draw a rectangle
    canvas.draw_polygon([a, (b[0], a[1]), b, (a[0], b[1])], border, borderClr)
    for i in range(a[0]+1, b[0]-1):
        canvas.draw_line((i, a[1]), (i, b[1]), 2, bgClr)

def RandRocks(): #generate rocks at random positions
    rr = []
    for i in range(random.randint(12)):
        x = random.randrange(0, canvasSize[0])
        y = random.randrange(0, canvasSize[1])
        while Inter.spaceship.zone()[1] <= x <= Inter.spaceship.zone()[3]: x = random.randrange(0, canvasSize[0])
        while Inter.spaceship.zone()[0] <= y <= Inter.spaceship.zone()[2]: y = random.randrange(0, canvasSize[1])
        rr.append(Rock.Rock((x, y), (0, 0)))
    return rr

Inter = Interaction(Spaceship.Spaceship((canvasSize[0]/2, canvasSize[1]/2), (0, 0)), RandRocks())

class Game:
    def __init__(self):
        self.welcomeScreen["enabled"] = True
        self.welcomeScreen = dict(enabled=True, x=canvasSize[0]/4, y=canvasSize[1]/4, width=canvasSize[0]/2, height=canvasSize[1]/2)
        self.score = 0

    def draw(self, canvas):
        if self.welcomeScreen["enabled"]: #display the welcome screen
            pass
            self.welcomeScreen["enabled"] = False
        else:
            Inter.draw(canvas)
            canvas.draw_text("Score: "+str(self.score), (canvasSize[0]-450, 50), 25, "White", "sans-serif")
            canvas.draw_text("Lives: "+str(Inter.spaceship.lives), (50, 50), 25, "White", "sans-serif")

    def mouse(self, p): #mouse handler
        if self.welcomeScreen["enabled"] and self.welcomeScreen["x"] <= p[0] <= self.welcomeScreen["x"]+self.welcomeScreen["width"] and self.welcomeScreen["y"] <= p[1] <= self.welcomeScreen["y"]+self.welcomeScreen["height"]:
            Inter.spaceship.lives = 3
            self.score = 0

    def keyDown(self, key): #key down handler
        global Inter
        if key == simplegui.KEY_MAP['left']: Inter.spaceship.rotCCW = True #spaceship rotates at a constant angular velocity in a counter clockwise direction
        if key == simplegui.KEY_MAP['right']: Inter.spaceship.rotCW = True #spaceship rotates at a constant angular velocity in a clockwise direction
        if key == simplegui.KEY_MAP['up']: Inter.spaceship.forward = True #spaceship accelerates in its forward direction
        if key == simplegui.KEY_MAP['space']: Inter.spaceship.gunLoaded = True #missile is spawned at the tip of the spaceship's gun

    def keyUp(self, key): #key up handler
        global Inter
        if key == simplegui.KEY_MAP['left']: Inter.spaceship.rotCCW = False
        if key == simplegui.KEY_MAP['right']: Inter.spaceship.rotCW = False
        if key == simplegui.KEY_MAP['up']: Inter.spaceship.forward = False
        if key == simplegui.KEY_MAP['space']: Inter.spaceship.gunLoaded = False

game = Game()

#Frame property specification
frame = simplegui.create_frame("Home", canvasSize[0], canvasSize[1])
frame.set_draw_handler(game.draw)
frame.set_mouseclick_handler(game.mouse)
frame.set_keydown_handler(game.keyDown)
frame.set_keyup_handler(game.keyUp)
frame.start()
