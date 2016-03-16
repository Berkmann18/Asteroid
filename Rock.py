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
time = 0

class Rock:
    def __init__(self, p=(0, 0), v=(0, 0), a=(0, 0)):
        """
        Rock class
        """
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.radius = 45
        self.exploded = False
        self.acc = Vector.Vector(a)
        self.frame_width = 10 #90/9
        self.frame_height = 10
        self.frame_index = [0, 0]

    def update(self):
        """
        Updates the position of the rock
        """
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        if self.exploded: #animate an explosion
            if self.frame_index[0] < 9:
                self.frame_index[1] += 1
                if self.frame_index[1] >= 9:
                    self.frame_index[1] %= 9
                    self.frame_index[0] += 1
            #print self.frame_index
        else:
            self.frame_index = [0, 0]
    def draw(self, canvas):
        """
        Draw the rock
        """
        if self.exploded:
            self.update()
            print(self.frame_index)
            canvas.draw_image(EXPLOSION_IMG, (self.frame_width*self.frame_index[1]+self.frame_width/2,\
				self.frame_height*self.frame_index[0]+self.frame_height/2),
                              (self.frame_width, self.frame_height), self.pos.get_pt(),\
                              (self.frame_width, self.frame_height))
        else:
            canvas.draw_image(IMG, (self.radius, self.radius), (self.radius*2, self.radius*2), self.pos.get_pt(),\
                              (self.radius*2, self.radius*2))
            self.vel.draw(canvas, self.pos.get_pt(), "Red")

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
        Collide with an other rock
        """
        vct_u = self.vel.copy()
        vct_v = rock.vel.copy()
        norm = self.pos.copy().sub(rock.pos).get_normal()
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
        Get the childs of that rock
        """
        childs = [
            Rock(self.pos.get_pt(), (2, 2)), Rock(self.pos.get_pt(), (2, -2)),
            Rock(self.pos.get_pt(), (-2, 2)), Rock(self.pos.get_pt(), (-2, -2))
        ]
        for child in childs:
            child.radius = self.radius/2
            child.update()

    def __str__(self):
        """
        String representation
        """
        return "Rock(pos="+str(self.pos)+", vel="+str(self.vel)+")"

def rand_rocks():
    """generate rocks at random positions"""
    rr = []
    for i in range(random.randint(12, 30)):
        x = random.randrange(0, CANVAS_SIZE[0])
        y = random.randrange(0, CANVAS_SIZE[1])
        pos = (x, y)
        rck = Rock(pos)
        rr.append(rck) #File 'user41_fvaKp4ptt1_6.py', Line 14: TypeError: '<invalid type>' does not support indexing
    return rr

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
        rck.draw_circ(canvas)

count = 0
def keydown():
    """Keydown handler"""
    global count
    if count < len(rocks) or len(rocks) > 0:
        rocks[count].exploded = True
        rocks[count].update()
        count += 1
        #rocks.pop(0)