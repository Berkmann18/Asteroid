"""
Spaceship.py
Module implementing the spaceship with its missiles
"""

try: #import SimpleGUI
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Util
import math
import Vector

IMG = simplegui.load_image("spaceship.png")
#^ or http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/double_ship.png
MISSILE_IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/shot3.png")
EXPLOSION_IMG = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/asteroids/explosion_spaceship.png")
IMG_SIZE = (180, 90)
IMG_CENTRE = (90, 45)
CANVAS_SIZE = (700, 500)

class Spaceship:
    def __init__(self, p, v=(0, 0), a=(0, 0)):
        self.pos = Vector.Vector(p) #position vector
        self.vel = Vector.Vector(v) #velocity vector
        self.lives = 3
        self.rotCW = False
        self.rotCCW = False
        self.forward = False
        self.gunLoaded = False
        self.missiles = []
        self.width = IMG_SIZE[0]/2 #2 columns
        self.height = IMG_SIZE[1]
        self.radius = IMG_CENTRE[1]
        self.acc = Vector.Vector(a) #acceleration vector
        self.orientation = Vector.Vector((0, 1))
        self.exploded = False

    def update(self):
        self.pos.add(self.vel)
        self.pos.x %= CANVAS_SIZE[0]
        self.pos.y %= CANVAS_SIZE[1]
        self.vel.add(self.acc)
        for m in self.missiles:
            m.update()
        if self.exploded: self.explode()

    def draw(self, canvas):
        if self.exploded:
            canvas.draw_image(EXPLOSION_IMG, (100*j+self.width/2, 100*i+self.height/2), (self.width, self.height), (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), (self.width, self.height))
        else:
            j = 1 if self.rotCCW or self.rotCW or self.forward else 0 #decide which image is going to be shown depending on the spaceship's state
            x = self.width*j+self.width/2
            y = self.height/2
            canvas.draw_image(IMG, (x, y), (self.width, self.height), self.pos.get_pt(), (self.width, self.height), self.orientation.x)
            for m in self.missiles: m.draw(canvas)
        self.vel.draw(canvas, self.pos.get_pt(), "blue")
        
    def hit(self, rock): #check whether or not the spaceship hit the rock
        return self.get_ball().hit(rock.get_ball())

    def offset(self, c): #boundaries of the image
        if c == 'l': return self.pos.x-self.width/2 #left side
        elif c == 'r': return self.pos.x+self.width/2 #right side
        elif c == 'u': return self.pos.y-self.height/2 #upper side
        else: return self.pos.y+self.height/2 #down side

    def zone(self): #zone around the spaceship
        #return [self.pos.y-self.height/2, self.pos.x-self.width/2, self.pos.y+self.height/2, self.pos.x+self.width/2]
        return util.Ball(self.pos, self.vel, self.radius*1.1, 1, "rgba(255, 255, 255, 0)", "blue")
        
    def shoot(self): #shoot a missile from the canon's position
        v = self.vel.copy()
        v.add(self.pos.copy().mult(IMG_SIZE[1]))
        """print v
        print self.orientation"""
        self.missiles.append(Missile((self.offset('d')+self.width+10, self.offset('u')+self.height/2), v.get_pt()))
    
    def draw_zone(self, canvas):
        #util.rect(canvas, (self.zone()[1], self.zone()[0]), (self.zone()[3], self.zone()[2]), 1, "blue", "rgba(255, 255, 255, 0)")
        self.zone().draw(canvas)
        
    def get_ball(self): #get the collision circle
        return util.Ball(self.pos, self.vel, .9*self.radius, 1, "rgba(255, 255, 255, 0)", "green")
    
    def draw_circ(self, canvas):
        """
        Draw the collision circle
        """
        self.get_ball().draw(canvas)
    
    def draw_vel(self, canvas):
        """
        Draw the velocity
        """
        pt = self.pos.copy().get_pt()
        #self.vel.draw(canvas, pt, "Red")
        canvas.draw_line(pt, (pt[0]+self.orientation.copy().mult(100).x, pt[1]+self.orientation.copy().mult(100).y), 3, "Red")
    def rot(self, theta):
        """
        Rotates the spaceship (in radians)
        """
        self.orientation = Vector.Vector((self.orientation.x*math.cos(theta)-self.orientation.y*math.sin(theta), self.orientation.x*math.sin(theta)+self.orientation.y*math.cos(theta)))
        self.orientation.x += self.orientation.x*math.cos(theta)-self.orientation.y*math.sin(theta)
        self.orientation.y += self.orientation.x*math.sin(theta)+self.orientation.y*math.cos(theta)
        
    def explode(self):
        """
        Explodes the spaceship
        """
        i = 0
        j = 0
        if i>=rows: timing = False #stop
        if timing:
            j += 1
            if j>=9:
                j %= 9
                i += 1
    
class Missile:
    def __init__(self, p, v):
        self.pos = Vector.Vector(p)
        self.vel = Vector.Vector(v)
        self.size = 20

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_image(MISSILE_IMG, (self.size/2, self.size/2), (self.size, self.size), self.pos.get_pt(), (self.size, self.size))

    def hit(self, asteroid): #check whether or not the missile reached a rock
        return self.get_ball().hit(asteroid.get_ball())

    def offset(self, c):
        if c == 'l': return self.pos.x-10
        elif c == 'r': return self.pos.x+10
        elif c == 'u': return self.pos.y-10
        else: return self.pos.y+10
'''
#Testing
def keydown(key):
    """
    Key down handler
    """
    if key == simplegui.KEY_MAP['left']:
        # Spaceship rotates at a constant angular velocity in a counter clockwise direction
        sc.rotCCW = True
    if key == simplegui.KEY_MAP['right']:
        # Spaceship rotates at a constant angular velocity in a clockwise direction
        sc.rotCW = True
    if key == simplegui.KEY_MAP['up']:
        # Spaceship accelerates in its forward direction
        sc.forward = True
    if key == simplegui.KEY_MAP['space']:
        # Missile is spawned at the tip of the spaceship's gun
        sc.gunLoaded = True

def keyup(key):
    """
    key up handler
    """
    if key == simplegui.KEY_MAP['left']:
        sc.rotCCW = False
    if key == simplegui.KEY_MAP['right']:
        sc.rotCW = False
    if key == simplegui.KEY_MAP['up']:
        sc.forward = False
    if key == simplegui.KEY_MAP['space']:
        sc.gunLoaded = False

def update():
    if sc.rotCW: #clockwise rotation of the spaceship
        sc.rot(0.17453) #.17453=10deg or 0.5236 for 30
    if sc.rotCCW: #counter clockwise rotation of the spaceship
        sc.rot(-0.17453) #-10deg
    if sc.forward: #go forward
        sc.update()
    if sc.gunLoaded: #shoot a missile
        sc.shoot()
        if sc.missiles[len(sc.missiles)-1].pos.x > CANVAS_SIZE[0]\
        or sc.missiles[len(sc.missiles)-1].pos.x < 0\
        or sc.missiles[len(sc.missiles)-1].pos.y > CANVAS_SIZE[1]\
        or sc.missiles[len(sc.missiles)-1].pos.y < 0:
            sc.missiles.pop() #remove the missile that went off-screen

def draw(canvas):
    update()
    sc.draw(canvas)
    sc.draw_circ(canvas)
    sc.draw_zone(canvas)
    sc.draw_vel(canvas)

sc = Spaceship((CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), (5, 0))
update()
frame = simplegui.create_frame("Spaceship", CANVAS_SIZE[0], CANVAS_SIZE[1])
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
'''