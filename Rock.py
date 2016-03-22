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
CANVAS_SIZE = (700, 500)

class Rock:
    def __init__(self, p=(0, 0), v=(0, 0), a=(0, 0), rad=45):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.radius = rad
        self.exploded = False
        self.acc = Vector.Vector(a)
        self.fully_exploded = False #Explosion completeness check
        self.ang = 0
        self.explosion_img = Util.ImgData("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/explosion_blue1.png", (3072, 128), 24, 1)
        self.explosion_img.size = (self.radius*2, self.radius*2)

    def update(self):
        """
        Update the rock
        """
        if Util.Clock.transit(60):
            self.pos.add(self.vel)
            self.vel.add(self.acc)
            if self.exploded:
                self.explosion_img.timing = True
                self.explosion_img.animate()
            else:
                self.explosion_img.reset()
            self.explosion_img.update()
            self.ang = (self.ang+.0008)%44
        self.fully_exploded = (self.exploded and self.explosion_img.complete)
        #print(self.explosion_img.i, self.explosion_img.j)

    def draw(self, canvas):
        """
        Draw the rock
        """
        if self.exploded:
            self.explosion_img.draw(canvas, self.pos.copy().get_pt())
        else:
            canvas.draw_image(IMG, (45, 45), (90, 90), self.pos.copy().get_pt(), (self.radius*2, self.radius*2), self.ang)

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
            rocks.append(c)

    def __str__(self):
        return "Rock(pos="+str(self.pos)+", vel="+str(self.vel)+")"

    def draw_vel(self, canvas):
        self.vel.draw(canvas, self.pos.copy().get_pt(), "Red")

def rand_rocks():
    """
    Generate rocks at random positions
    """
    arr = []
    for i in range(random.randint(8, 12)):
        x = random.randrange(0, CANVAS_SIZE[0])
        y = random.randrange(0, CANVAS_SIZE[1])
        arr.append(Rock((x, y), (0, 0), (0, 0), random.randint(10, 45)))
    return arr

rocks = rand_rocks()

def drawRocks(canvas):
    for r in rocks:
        for r0 in rocks:
            if not r==r0 and r.hit(r0):
                r.collide(r0)
                #r0.get_child()
            r0.update()
            r.update()
        r.draw(canvas)
        r.draw_circ(canvas)
        r.draw_vel(canvas)
'''
def kd(key):
    if len(rocks)>0:
        rocks[0].exploded = True
        rocks[0].update()
        rocks[0].explosion_img.update()
        print "fe:", rocks[0].fully_exploded
        print "cpl:", rocks[0].explosion_img.complete
        print "done:", rocks[0].explosion_img.is_done()
        if rocks[0].fully_exploded:
            #rocks[0].update()
            rocks.pop(0)
            print "-1"

frame = simplegui.create_frame("Rocks", 700, CANVAS_SIZE[1])
frame.set_draw_handler(drawRocks)
frame.set_keydown_handler(kd)
frame.start()'''