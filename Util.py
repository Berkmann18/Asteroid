"""
Util.py
An utilitary module
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2PyGAME.simpleguics2pygame as simplegui

import Vector

class clock:
    """
    Game loop clock
    """
    def __init__(self):
        self.time = 0
        self.rate = 0

    def tick(self):
        self.time += 1

    def transit(self, frameRate):
        self.tick()
        self.fr = 60/frameRate
        return self.time%self.fr==0

Clock = clock()

class ImgData:
    """
    Data collection of an image
    """
    def __init__(self, src, sz=(64, 64), c=1, r=1, sI=0, sJ=0):
        self.src = simplegui.load_image(src)
        self.size = sz
        self.cols = c
        self.rows = r
        self.i = sI
        self.j = sJ
        self.frame_width = self.size[0]/self.cols
        self.frame_height = self.size[1]/self.rows
        self.x = self.frame_width*self.j+self.frame_width/2
        self.y = self.frame_height*self.i+self.frame_height/2
        self.timing = False
        self.complete = False
        self.frate = 50
        #self.size = (self.frame_width, self.frame_height) for some reason this line get both fields to 9

    def update(self):
        """
        Update the image's data
        """
        self.frame_width = self.size[0]/self.cols
        self.frame_height = self.size[1]/self.rows
        self.x = self.frame_width*self.j+self.frame_width/2
        self.y = self.frame_height*self.i+self.frame_height/2
        self.complete = True if self.is_done() else False
        #self.size = (self.frame_width, self.frame_height)

    def draw(self, canvas, pos=(0, 0), rot=0):
        """
        Draw the image
        """#image, center_source, width_height_source, center_dest, width_height_dest
        if self.cols==1 and self.rows==1: #image
            canvas.draw_image(self.src, (self.frame_width/2, self.frame_height/2), (self.frame_width, self.frame_height), pos, (self.frame_width, self.frame_height), rot)
        else: #sprite
            canvas.draw_image(self.src, (self.x, self.y), (self.frame_width, self.frame_height), pos, (self.frame_width, self.frame_height), rot)

    def i_plus(self):
        """
        Increment the frame index i
        """
        self.i += 1

    def i_minus(self):
        """
        Decrement the frame index i
        """
        self.i -= 1

    def j_plus(self):
        """
        Increment the frame index j
        """
        self.j += 1
    def j_minus(self):
        """
        Decrement the frame index j
        """
        self.j -= 1

    def animate(self):
        """
        Animate the image
        """
        if Clock.transit(self.frate):
            if self.i >= self.rows and self.j >= self.cols and not self.timing: #reset
                self.i = 0
                self.j = 0
            if self.i >= self.rows:
                self.timing = False #stop
                self.complete = True
            if self.timing:
                self.j += 1
                if self.j >= self.cols:
                    self.j %= self.cols
                    self.i += 1
            self.update()

    def unanimate(self):
        """
        Reverse animation
        """
        if Clock.transit(self.frate):
            if self.i <= 0 and self.j <= 0 and not self.timing: #reset
                self.i = self.rows
                self.j = self.cols
            if self.i <= 0:
                self.timing = False #stop
                self.complete = True
            if self.timing:
                self.j -= 1
                if self.j <= 0:
                    self.j %= self.cols
                    self.i -= 1
            self.update()

    def toggle(self):
        """
        Switch on/off the timing
        """
        self.timing = False if self.timing else True

    def run(self, canvas, pos=(0, 0), theta=0):
        """
        Show the animation
        """
        self.draw(canvas, pos, theta)
        self.animate()

    def reset(self):
        """
        Reset everything needed
        """
        self.i = 0
        self.j = 0
        self.timing = False
        self.update()

    def get_frame_index(self):
        """
        Get the frame index
        """
        return (self.i, self.j)

    def is_done(self):
        return self.complete or (self.i>=self.cols and self.j>=0)

def rect(canvas, pt_a, pt_b, border=1, border_clr="Black", bg_clr="White"):
    """
    Draw a rectangle
    """
    canvas.draw_polygon([pt_a, (pt_b[0], pt_a[1]), pt_b, (pt_a[0], pt_b[1])],\
    border, border_clr)
    for i in range(pt_a[0]+1, pt_b[0]-1):
        canvas.draw_line((i, pt_a[1]), (i, pt_b[1]), 2, bg_clr)

class Ball:
    """
    Ball class
    """
    def __init__(self, pos, vel, radius, border, color, color2):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.border = border
        self.color = color
        self.border_color = color2
        self.lives = 10

    def update(self):
        """
        Update the ball's position
        """
        self.pos.add(self.vel)

    def offset_l(self):
        """
        Left offset
        """
        return self.pos.x - self.radius

    def offset_r(self):
        """
        Right offset
        """
        return self.pos.x + self.radius

    def offset_u(self):
        """
        Upper offset
        """
        return self.pos.y - self.radius

    def offset_d(self):
        """
        Bottom offset
        """
        return self.pos.y + self.radius

    def draw(self, canvas):
        """
        Draw the ball
        """
        canvas.draw_circle(self.pos.get_pt(), self.radius, self.border,\
                           self.border_color, self.color)

    def bounce(self, normal):
        """
        Bounce the ball
        """
        self.vel.reflect(normal)

    def hit(self, ball):
        """
        Ball/ball collision detection
        """
        return self.pos.copy().sub(ball.pos).length() <= self.radius+ball.radius

def print_list(lst):
    """
    print a non-native typed list
    """
    str = ""
    for i in lst:
        str += i.__str__()+", "
    print(str)
