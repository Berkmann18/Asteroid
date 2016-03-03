"""
Rock.py
The module that implements asteroids
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Vector

IMG = simplegui.load_image("\
http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/asteroid_blue.png")

class Rock:
    """
    Rock class
    """
    def __init__(self, p, v):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.size = 90

    def update(self):
        """
        Updates the position of the rock
        """
        self.pos.add(self.vel)

    def draw(self, canvas):
        """
        Draw the rock
        """
        canvas.draw_image(IMG, (self.size/2, self.size/2), (self.size, self.size),\
        self.pos.get_pt(), (self.size, self.size))

    def offset(self, char):
        """
        Offsets of the rock
        """
        if char == 'l':
            return self.pos.x_coord-self.size/2
        elif char == 'r':
            return self.pos.x_coord+self.size/2
        elif char == 'u':
            return self.pos.y_coord-self.size/2
        else:
            return self.pos.y_coord+-self.size/2
