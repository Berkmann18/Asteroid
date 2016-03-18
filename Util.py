"""
Util.py
An utilitary module
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2PyGAME.simpleguics2pygame as simplegui

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
        self.frameWidth = self.size[0]/self.cols
        self.frameHeight = self.size[1]/self.rows
        self.x = self.frameWidth*self.j+self.frameWidth/2
        self.y = self.frameHeight*self.i+self.frameHeight/2
        self.timing = False
        self.complete = False

    def update(self):
        """
        Update the image's data
        """
        self.frameWidth = self.size[0]/self.cols
        self.frameHeight = self.size[1]/self.rows
        self.x = self.frameWidth*self.j+self.frameWidth/2
        self.y = self.frameHeight*self.i+self.frameHeight/2
        self.complete = True if (self.i >= self.cols and self.j >= self.rows) else False

    def draw(self, canvas, pos=(0, 0), rot=0):
        """
        Draw the image
        """
        canvas.draw_image(self.src, (self.x, self.y), (self.frameWidth, self.frameHeight), pos, (self.frameWidth, self.frameHeight), rot)

    def ip(self):
        """
        Increment the frame index i
        """
        self.i += 1

    def im(self):
        """
        Decrement the frame index i
        """
        self.i -= 1

    def jp(self):
        """
        Increment the frame index j
        """
        self.j += 1
    def jm(self):
        """
        Decrement the frame index j
        """
        self.j -= 1

    def animate(self):
        """
        Animate the image
        """
        if self.i>=self.rows and self.j>=self.cols and self.timing==False: #reset
            self.i = 0
            self.j = 0
        if self.i>=self.rows: self.timing = False #stop
        if self.timing:
            self.j += 1
            if self.j>=self.cols:
                self.j %= self.cols
                self.i += 1
        self.update()

    def unanimate(self):
        """
        Reverse animation
        """
        if self.i<=0 and self.j<=0 and self.timing==False: #reset
            self.i = self.rows
            self.j = self.cols
        if self.i<=0: self.timing = False #stop
        if self.timing:
            self.j -= 1
            if self.j<=0:
                self.j %= self.cols
                self.i -= 1
        self.update()

    def toggle(self):
        self.timing = False if self.timing else True

    def run(self, canvas, pos=(0, 0)):
        self.draw(canvas, pos)
        self.animate()

    def reset(self):
        self.i = 0
        self.j = 0
        self.timing = False
        self.update()

    def get_frame_index(self):
        return (self.i, self.j)

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
