"""
Rock.py
The module that implements asteroids
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Util
import Vector

IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/asteroid_brown.png")

class Rock:
    """
    Rock class
    """
    def __init__(self, p, v):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.radius = 45

    def update(self):
        """
        Updates the position of the rock
        """
        self.pos.add(self.vel)

    def draw(self, canvas):
        """
        Draw the rock
        """
        canvas.draw_image(IMG, (self.radius, self.radius), (self.radius*2, self.radius*2),\
                          self.pos.get_pt(), (self.radius*2, self.radius*2))

    def offset(self, char):
        """
        Offsets of the rock
        """
        if char == 'l':
            return self.pos.x-self.radius
        elif char == 'r':
            return self.pos.x+self.radius
        elif char == 'u':
            return self.pos.y-self.radius
        else:
            return self.pos.y+self.radius

    def get_ball(self):
        """
        Get the collision circle
        """
        return Util.Ball(self.pos, self.vel, .8*self.radius, 1, "rgba(255, 255, 255, 0)", "red")

    def draw_circ(self, canvas):
        """
        Draw the collision circle
        """
        self.get_ball().draw(canvas)

    def collide(self, rock):
        """
        Collide against an other rock
        """
        vct_u = self.vel.copy()
        vct_v = rock.vel.copy()
        norm = (self.pos.copy().sub(rock.pos)).get_normal()
        vct_z = norm.copy().mult(self.pos.copy().sub(rock.pos).dot(norm))

        vct_u.add(vct_z)
        vct_v.sub(vct_z)

        self.vel = vct_u
        rock.vel = vct_v

    def hit(self, rck):
        """
        Rock/rock collision detection
        """
        return self.get_ball().hit(rck.get_ball())

    def get_child(self):
        """
        Make 4 childrens that goes different ways
        """
        childs = [
            Rock(self.pos.get_pt(), (2, 2)), Rock(self.pos.get_pt(), (2, -2)),
            Rock(self.pos.get_pt(), (-2, 2)), Rock(self.pos.get_pt(), (-2, -2))
        ]
        for child in childs:
            child.radius = self.radius/2
            child.update()
