#Main class

import random, Vector, Spaceship, Rock
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
        self.spaceship.update()
        for r in self.rocks:
            r.update()
            if r.hit(self.spaceship):
                self.spaceship.lives -= 1 #take a life off the spaceship and ...


def welcomeScreen(): #display the welcome screen
    pass

def RandRocks():
    rr = []
    for i in random.randint(12):
        x = random.randrange(0, canvasSize[0])
        y = random.randrange(0, canvasSize[1])
        rr.append(Rock((x, y), (0, 0)))
    return rr

Inter = Interaction(Spaceship((canvasSize[0]/2, canvasSize[1]/2), (0, 0)), RandRocks())
frame = simplegui.create_frame("Home", canvasSize[0], canvasSize[1])
frame.set_draw_handler(Inter.draw)

frame.start()
