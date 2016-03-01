#Main class
import simplegui

class Interaction:
    def __init__(self, spaceship, rocks):
        self.spaceship = spaceship
        self.rocks = rocks
        self.inCollision = False

    def draw(self, canvas):
        self.spaceship.draw(canvas)
        for r in self.rocks: r.draw(canvas)

    def update(self):
        self.spaceship.update()
        for r in self.rocks:
            r.update()
            if r.hit(self.spaceship):
                if not self.inCollision:
                    #take a life off the spaceship and ...
                    self.inCollision = True
            else: self.inCollision = False

def welcomeScreen(): #display the welcome screen
    pass

frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)

frame.start()
