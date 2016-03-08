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
        self.border = 1
        self.color = color
        self.borderColor = color2
        self.lives = 10

    def update(self):
        """
        Updates the ball's position
        """
        self.pos.add(self.vel)

    def offsetL(self):
        """
        Left offset
        """
        return self.pos.x - self.radius

    def offsetR(self):
        """
        Right offset
        """
        return self.pos.x + self.radius

    def offsetU(self):
        """
        Top offset
        """
        return self.pos.y - self.radius

    def offsetD(self):
        """
        Bottom offset
        """
        return self.pos.y + self.radius

    def draw(self, canvas):
        """
        Draw the ball
        """
        canvas.draw_circle(self.pos.getP(), self.radius, self.border, self.borderColor, self.color)

    def bounce(self, normal):
        """
        Make the ball bounce
        """
        self.vel.reflect(normal)

    def hit(self, ball):
        """
        Ball/ball collision detection
        """
        return self.pos.copy().sub(ball.pos).length() <= self.radius+ball.radius
