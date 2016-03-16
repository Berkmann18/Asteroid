"""
Spaceship.py
Module implementing the spaceship with its missiles
"""

try: #import SimpleGUI
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Util
import Vector

IMG = simplegui.load_image("spaceship.png")
#^ or http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/double_ship.png
MISSILE_IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/shot3.png")
EXPLOSION_IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/explosion_spaceship.png")
IMG_SIZE = (180, 90)
IMG_CENTRE = (90, 45)
CANVAS_SIZE = (700, 500)

class Spaceship:
    """
    Spaceship class
    """
    def __init__(self, pos=(0, 0), vel=(0, 0), acc=(0, 0)):
        self.pos = Vector.Vector(pos) #position vector
        self.vel = Vector.Vector(vel) #velocity vector
        self.lives = 3
        self.rot_cw = False
        self.rot_ccw = False
        self.forward = False
        self.gun_loaded = False
        self.missiles = []
        self.width = IMG_SIZE[0]/2 #2 columns
        self.height = IMG_SIZE[1]
        self.radius = IMG_SIZE[1]
        self.acc = Vector.Vector(acc) #acceleration vector
        self.orientation = Vector.Vector((0, 1))
        self.exploded = False

    def update(self):
        """
        Update the position of the spaceship as well as anything related to it
        """
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        for msl in self.missiles:
            msl.update()
        if self.exploded:
            self.explode()

    def draw(self, canvas):
        """
        Draw the spaceship and its missiles
        """
        # Decide which image is going to be shown depending on the spaceship's state
        if self.exploded:
            canvas.draw_image(EXPLOSION_IMG, (100*j+self.width/2, 100*i+self.height/2), (self.width, self.height), (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), (self.width, self.height))
        else:
            j = 1 if self.rot_ccw or self.rot_cw or self.forward else 0 #decide which image is going to be shown depending on the spaceship's state
            x = self.width*j+self.width/2
            y = self.height/2
            canvas.draw_image(IMG, (x, y), (self.width, self.height), self.pos.get_pt(), (self.width, self.height), self.orientation.x)
            for msl in self.missiles:
                msl.draw(canvas)
        self.get_ball().draw(canvas)
        self.vel.draw(canvas, self.pos.get_pt(), "blue")

    def hit(self, rock):
        """
        Check whether or not the spaceship hit the rock
        """
        return self.get_ball().hit(rock.get_ball())

    def offset(self, char):
        """
        Boundaries of the image
        """
        if char == 'l':
            return self.pos.x-self.width/2 #left side
        elif char == 'r':
            return self.pos.x+self.width/2 #right side
        elif char == 'u':
            return self.pos.y-self.height/2 #upper side
        else:
            return self.pos.y+self.height/2 #down side

    def zone(self):
        """
        Zone around the spaceship
        """
        return [self.pos.y-self.height, self.pos.x-self.width,\
        self.pos.y+self.height, self.pos.x+self.width] #u, l, d, r

    def shoot(self):
        """
        shoot a missile from the canon's position
        """
        vct = self.vel.copy()
        vct.add(self.pos.copy().mult(IMG_SIZE[1]))
        self.missiles.append(Missile((self.offset('d')+self.width+10, self.offset('u')+self.height/2), vct.get_pt()))

    def get_ball(self):
        """
        Get the collision circle
        """
        return Util.Ball(self.pos, self.vel, .9*self.radius, 1, "rgba(255, 255, 255, 0)", "green")

    def rot(self, theta): #in radians
        """
        Rotate the spaceship
        """
        self.orientation.rot(theta)

    def explode(self):
        """
        Explode the spaceship
        """
        i = 0
        j = 0
        if self.exploded:
            j += 1
            if j >= 9:
                j %= 9
                i += 1

class Missile:
    """
    Missile class
    """
    def __init__(self, pos, vel):
        self.pos = Vector.Vector(pos)
        self.vel = Vector.Vector(vel)
        self.size = 20

    def update(self):
        """
        Update the position of the missile
        """
        self.pos.add(self.vel)

    def draw(self, canvas):
        """
        Draw the missile
        """
        canvas.draw_image(MISSILE_IMG, (10, 10), (20, 20), self.pos.get_pt(), (20, 20))

    def hit(self, asteroid):
        """
        Check whether or not the missile reached a rock
        """
        return not ((asteroid.pos.x > self.pos.x+self.size) or\
        (asteroid.pos.x+asteroid.radius < self.pos.x) or\
        (asteroid.pos.y > self.pos.y+self.size) or\
        (asteroid.pos.y+asteroid.radius < self.pos.y))

    def offset(self, char):
        """
        Offsets of the missile
        """
        if char == 'l':
            return self.pos.x-10
        elif char == 'r':
            return self.pos.x+10
        elif char == 'u':
            return self.pos.y-10
        else:
            return self.pos.y+10
