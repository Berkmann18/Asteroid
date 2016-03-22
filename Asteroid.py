"""
Asteroid.py
Main class of the Asteroid GAME
"""

import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2PyGAME.simpleguics2pygame as simplegui

import Rock
import Spaceship

CANVAS_SIZE = (700, 500)
BG_IMG = Util.ImgData("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png", (800, 600))

class Interaction:
    """
    Interaction between the spaceship and the rocks
    """
    def __init__(self, spaceship, rocks):
        self.spaceship = spaceship
        self.rocks = rocks

    def draw(self, canvas):
        """
        Draw everything needed for the interaction
        """
        BG_IMG.draw(canvas, (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2))
        self.spaceship.draw(canvas)
        self.spaceship.draw_circ(canvas)
        #self.spaceship.draw_vel(canvas)
        #self.spaceship.draw_zone(canvas)
        for rocks in self.rocks:
            rocks.draw(canvas)
            rocks.draw_circ(canvas)
            #rocks.draw_vel(canvas)

    def update(self):
        """
        Update everything needed for the interaction
        """
        for r in self.rocks:
            if r.fully_exploded:
                rocks.pop(rocks.index(r))
                GAME.score += 1
            for r0 in self.rocks:
                r.update()
                r0.update()
                if not r==r0 and r.hit(r0):
                    #print "" #anti-bug to avoid having rocks still colliding
                    r.collide(r0)
                    r0.get_child()
            if self.spaceship.hit(r):
                self.spaceship.lives -= 1 #take a life off the spaceship
                r.exploded = True
        if self.spaceship.lives <= 0: #start over
            GAME.welcome_screen["enabled"] = True
            self.rocks = [] #remove all rocks

        if self.spaceship.rotCW: #clockwise rotation of the spaceship
            self.spaceship.rot(0.17453) #10deg
        if self.spaceship.rotCCW: #counter clockwise rotation of the spaceship
            self.spaceship.rot(-0.17453) #-10deg
        if self.spaceship.forward: #go forward
            self.spaceship.update()
        if self.spaceship.gunLoaded: #shoot a missile
            self.spaceship.shoot()
            if self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x > CANVAS_SIZE[0]\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x < 0\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y > CANVAS_SIZE[1]\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y < 0:
                self.spaceship.missiles.pop() #remove the missile that went off-screen

def rand_rocks():
    """
    Generate rocks at random positions
    """
    arr = []
    for i in range(random.randint(0, 12)):
        x = random.randrange(11, CANVAS_SIZE[0]-11)
        y = random.randrange(11, CANVAS_SIZE[1]-11)
        while INTER.spaceship.zone().radius-INTER.spaceship.zone().pos.x <= x <= INTER.spaceship.zone().radius+INTER.spaceship.zone().pos.x:
            x = random.randrange(0, CANVAS_SIZE[0])
        while INTER.spaceship.zone().radius-INTER.spaceship.zone().pos.y <= y <= INTER.spaceship.zone().radius+INTER.spaceship.zone().pos.y:
            y = random.randrange(0, CANVAS_SIZE[1])
        arr.append(Rock.Rock((x, y), (0, 0), (0, 0), random.randint(10, 45)))
    return arr

INTER = Interaction(Spaceship.Spaceship((CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), (0, 0)), [])
INTER.rocks = rand_rocks()

class Game:
    """
    Game class containing the UI and key management system
    """
    def __init__(self):

        self.welcome_screen = {
            "enabled": True,
            "x": CANVAS_SIZE[0]/2,
            "y": CANVAS_SIZE[1]/2,
            "width": 941,
            "height": 473,
            "img": simplegui.load_image("http://s23.postimg.org/vvz9p8o0r/splash.png")
        }
        self.score = 0
        self.time = 0
        self.timerRunning = False

    def draw(self, canvas):
        """
        UI
        """
        if self.welcome_screen["enabled"]: #display the welcome screen
            #image, center_source, width_height_source, center_dest, width_height_dest
            canvas.draw_image(self.welcome_screen["img"], (self.welcome_screen["width"]/2, self.welcome_screen["height"]/2), (self.welcome_screen["width"], self.welcome_screen["height"]), (self.welcome_screen["x"], self.welcome_screen["y"]), (self.welcome_screen["x"], self.welcome_screen["y"]))
        else:
            INTER.draw(canvas)
            canvas.draw_text("Score: "+str(self.score),\
            (CANVAS_SIZE[0]-100, 50), 25, "White", "sans-serif")
            canvas.draw_text("Lives: "+str(INTER.spaceship.lives),\
            (50, 50), 25, "White", "sans-serif")

    def mouse(self, pos):
        """
        Mouse handler
        """
        if self.welcome_screen["enabled"] and\
        self.welcome_screen["x"]-self.welcome_screen["width"]/2 <= pos[0] <= self.welcome_screen["x"]+self.welcome_screen["width"]/2\
        and self.welcome_screen["y"]-self.welcome_screen["height"]/2 <= pos[1] <= self.welcome_screen["y"]+self.welcome_screen["height"]/2:
            self.welcome_screen["enabled"] = False
            INTER.spaceship.lives = 3
            self.score = 0

    def toggleTimer(self):
        self.running = False if self.running else True

def keydown(key):
    """
    Key down handler
    """
    if key == simplegui.KEY_MAP['left']:
        # Spaceship rotates at a constant angular velocity in a counter clockwise direction
        INTER.spaceship.rotCCW = True
    if key == simplegui.KEY_MAP['right']:
        # Spaceship rotates at a constant angular velocity in a clockwise direction
        INTER.spaceship.rotCW = True
    if key == simplegui.KEY_MAP['up']:
        # Spaceship accelerates in its forward direction
        INTER.spaceship.forward = True
    if key == simplegui.KEY_MAP['space']:
        # Missile is spawned at the tip of the spaceship's gun
        INTER.spaceship.gunLoaded = True

def keyup(key):
    """
    key up handler
    """
    if key == simplegui.KEY_MAP['left']:
        INTER.spaceship.rotCCW = False
    if key == simplegui.KEY_MAP['right']:
        INTER.spaceship.rotCW = False
    if key == simplegui.KEY_MAP['up']:
        INTER.spaceship.forward = False
    if key == simplegui.KEY_MAP['space']:
        INTER.spaceship.gunLoaded = False

GAME = Game()
INTER.update()

#Frame property specification
FRAME = simplegui.create_frame("Asteroid", CANVAS_SIZE[0], CANVAS_SIZE[1])
FRAME.set_draw_handler(GAME.draw)
FRAME.set_mouseclick_handler(GAME.mouse)
FRAME.set_keydown_handler(keydown)
FRAME.set_keyup_handler(keyup)
FRAME.start()
