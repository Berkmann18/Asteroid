"""
Asteroid.py
Main class of the Asteroid GAME
"""

import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2PyGAME.simpleguics2pyGAME as simplegui

import Rock
import Spaceship

CANVAS_SIZE = (600, 400)

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
        self.spaceship.draw(canvas)
        for rocks in self.rocks:
            rocks.draw(canvas)

    def update(self):
        """
        Update everything needed for the interaction
        """
        for rocks in self.rocks:
            if self.spaceship.hit(rocks):
                self.spaceship.lives -= 1 #take a life off the spaceship
        if self.spaceship.lives <= 0: #start over
            GAME.welcome_screen["enabled"] = True
            self.rocks = [] #remove all rocks

        if self.spaceship.rotCW: #clockwise rotation of the spaceship
            pass
        if self.spaceship.rotCCW: #counter clockwise rotation of the spaceship
            pass
        if self.spaceship.forward: #go forward
            self.spaceship.update()
        if self.spaceship.gunLoaded: #shoot a missile
            self.spaceship.shoot()
            if self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x_coord > CANVAS_SIZE[0]\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.x_coord < 0\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y_coord > CANVAS_SIZE[1]\
            or self.spaceship.missiles[len(self.spaceship.missiles)-1].pos.y_coord < 0:
                self.spaceship.missiles.pop() #remove the missile that went off-screen


def rect(canvas, pt_a, pt_b, pt_border, pt_border_clr, pt_bg_clr):
    """
    Drpt_aw pt_a rectpt_angle
    """
    canvas.draw_polygon([pt_a, (pt_b[0], pt_a[1]), pt_b, (pt_a[0], pt_b[1])],\
	pt_border, pt_border_clr)
    for i in range(pt_a[0]+1, pt_b[0]-1):
        canvas.draw_line((i, pt_a[1]), (i, pt_b[1]), 2, pt_bg_clr)

def randrocks():
    """
    Generate rocks at random positions
    """
    arr = []
    for i in range(random.randint(0, 12)):
        x_coord = random.randrange(0, CANVAS_SIZE[0])
        y_coord = random.randrange(0, CANVAS_SIZE[1])
        while INTER.spaceship.zone()[1] <= x_coord <= INTER.spaceship.zone()[3]:
            x_coord = random.randrange(0, CANVAS_SIZE[0])
        while INTER.spaceship.zone()[0] <= y_coord <= INTER.spaceship.zone()[2]:
            y_coord = random.randrange(0, CANVAS_SIZE[1])
        arr.append(Rock.Rock((x_coord, y_coord), (0, 0)))
    return arr

INTER = Interaction(Spaceship.Spaceship((CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), (0, 0)), randrocks())

class Game:
    """
    Game class containing the UI and key management system
    """
    def __init__(self):
        self.welcome_screen = dict(enabled=True, x=CANVAS_SIZE[0]/4,\
        y=CANVAS_SIZE[1]/4, width=CANVAS_SIZE[0]/2,\
        height=CANVAS_SIZE[1]/2)
        self.score = 0

    def draw(self, canvas):
        """
        UI
        """
        if self.welcome_screen["enabled"]: #display the welcome screen
            self.welcome_screen["enabled"] = False
        else:
            INTER.draw(canvas)
            canvas.draw_text("Score: "+str(self.score),\
			(CANVAS_SIZE[0]-450, 50), 25, "White", "sans-serif")
            canvas.draw_text("Lives: "+str(INTER.spaceship.lives),\
			(50, 50), 25, "White", "sans-serif")

    def mouse(self, pos):
        """
        Mouse handler
        """
        if self.welcome_screen["enabled"] and\
		self.welcome_screen["x"] <= pos[0] <= self.welcome_screen["x"]+self.welcome_screen["width"]\
		and self.welcome_screen["y"] <= pos[1] <= self.welcome_screen["y"]+self.welcome_screen["height"]:
            INTER.spaceship.lives = 3
            self.score = 0

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

#Frame property specification
FRAME = simplegui.create_frame("Asteroid", CANVAS_SIZE[0], CANVAS_SIZE[1])
FRAME.set_draw_handler(GAME.draw)
FRAME.set_mouseclick_handler(GAME.mouse)
FRAME.set_keydown_handler(keydown)
FRAME.set_keyup_handler(keyup)
FRAME.start()
