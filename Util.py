"""
Util.py
An utilitary module
"""

def rect(canvas, pt_a, pt_b, pt_border, pt_border_clr, pt_bg_clr):
    """
    Draw a rectangle
    """
    canvas.draw_polygon([pt_a, (pt_b[0], pt_a[1]), pt_b, (pt_a[0], pt_b[1])],\
    pt_border, pt_border_clr)
    for i in range(pt_a[0]+1, pt_b[0]-1):
        canvas.draw_line((i, pt_a[1]), (i, pt_b[1]), 2, pt_bg_clr)

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
