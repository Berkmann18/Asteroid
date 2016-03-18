"""
Rock.py
The module that implements asteroids
"""

import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Util
import Vector

IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/asteroid_brown.png")
EXPLOSION_IMG = simplegui.load_image("\
http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/explosion_blue1.png")
CANVAS_SIZE = (700, 500)

class Rock:
    def __init__(self, p=(0, 0), v=(0, 0), a=(0, 0)):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.radius = 45
        self.exploded = False
        self.acc = Vector.Vector(a)
        self.fully_exploded = False #Explosion completeness check
        self.ang = 0
        self.explosion_img = Util.ImgData("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/explosion_blue1.png",\
        (3072, 128), 24, 1)
 
    def update(self):
        """
        Update the rock
        """
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        if self.exploded:
            self.explosion_img.timing = True
            self.explosion_img.animate()
        else:
            pass#self.explosion_img.reset()
        self.explosion_img.update()
        self.fully_exploded = (self.exploded and self.explosion_img.complete)
        self.ang = (self.ang+.1)%44
        #print(self.explosion_img.i, self.explosion_img.j)

    def draw(self, canvas):
        """
        Draw the rock
        """
        if self.exploded:
            self.explosion_img.draw(canvas, self.pos.copy().get_pt())
        else:
            canvas.draw_image(IMG, (self.radius, self.radius), (self.radius*2, self.radius*2), self.pos.copy().get_pt(), (self.radius*2, self.radius*2), self.ang)
            self.vel.draw(canvas, self.pos.copy().get_pt(), "Red")

    def offset(self, char):
        """
        Get the offset
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
        Rock/rock collision
        """
        u = self.vel.copy()
        v = rock.vel.copy()
        n = self.pos.copy().sub(rock.pos).get_normal()
        z = n.copy().mult(self.pos.copy().sub(rock.pos).dot(n))

        u.add(z)
        v.sub(z)

        self.vel = u
        rock.vel = v

    def hit(self, rck):
        """
        Rock/rock collision detection
        """
        return self.get_ball().hit(rck.get_ball())

    def get_child(self):
        """
        Generate the childs
        """
        childs = [
            Rock(self.pos.get_pt(), (2, 2)), Rock(self.pos.get_pt(), (2, -2)),
            Rock(self.pos.get_pt(), (-2, 2)), Rock(self.pos.get_pt(), (-2, -2))
        ]
        for c in childs:
            c.radius = self.radius/2
            c.update()

    def __str__(self):
        return "Rock(pos="+str(self.pos)+", vel="+str(self.vel)+")"

def rand_rocks():
    """generate rocks at random positions"""
    rdrck = []
    for i in range(random.randint(12, 30)):
        x = random.randrange(0, CANVAS_SIZE[0])
        y = random.randrange(0, CANVAS_SIZE[1])
        pos = (x, y)
        rck = Rock(pos)
        rdrck.append(rck)
    return rdrck

rocks = rand_rocks()

def draw_rocks(canvas):
    """Draw the rocks"""
    for rck in rocks:
        for rck0 in rocks:
            if not rck == rck0 and rck.hit(rck0):
                rck.collide(rck0)
                rck0.get_child()
            rck.update()
            rck0.update()
        rck.draw(canvas)
        #rck.draw_circ(canvas)

def keydown():
    """Keydown handler"""
    if len(rocks) > 0:
        rocks[0].exploded = True
        rocks[0].update()
        if rocks[0].fully_exploded:
            rocks.pop(0)
