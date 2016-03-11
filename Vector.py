"""
Vector.py
The module that implements vectors and all the necessary methods that comes with vectors.
"""

import math

class Vector:
    """
    The Vector class
    """
    # Initialiser
    def __init__(self, p=(0, 0)):
        self.x = p[0]
        self.y = p[1]

    @property
    def __str__(self):
        """
        Returns a string representation of the vector
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        """
        Tests the equality of this vector and another
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Tests the inequality of this vector and another
        """
        return not self.__eq__(other)

    def get_pt(self):
        """
        Returns a tuple with the point corresponding to the vector
        """
        return (self.x, self.y)

    def copy(self):
        """
        Returns a copy of the vector
        """
        vct = Vector()
        vct.x = self.x
        vct.y = self.y
        return vct

    def mult(self, k):
        """
        Multiplies the vector by a scalar
        """
        self.x *= k
        self.y *= k
        return self

    def div(self, k):
        """
        Divides the vector by a scalar
        """
        self.x /= k
        self.y /= k
        return self

    def normalise(self):
        """
        Normalizes the vector
        """
        vct = math.sqrt(self.x**2 + self.y**2)
        self.x /= vct
        self.y /= vct

    @property
    def get_normalised(self):
        """
        Returns a normalized version of the vector
        """
        return [self.x / math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)),
                self.y / math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))]

    @property
    def get_normal(self):
        """
        Returns the normal of the vector
        """
        return Vector(self.get_normalised)

    def add(self, other):
        """
        Vector addition
        """
        self.x += other.x
        self.y += other.y
        return self

    def sub(self, other):
        """
        Vector substraction
        """
        self.x -= other.x
        self.y -= other.y
        return self

    def zero(self):
        """
        Reset to the zero vector
        """
        self.x = 0
        self.y = 0
        return self

    def negate(self):
        """
        Negates the vector (makes it point in the opposite direction)
        """
        self.x = -self.x
        self.y = -self.y
        return self

    def dot(self, other):
        """
        Scalar/dot product
        """
        return self.x*other.x + self.y*other.y

    def length(self):
        """
        Returns the length of the vector
        """
        return math.sqrt(self.length_sq())

    def length_sq(self):
        """
        Returns the squared length of the vector
        """
        return self.x**2 + self.y**2

    def reflect(self, normal):
        """
        Reflection on a normal
        """
        norm = normal.copy
        norm.mult(2*self.dot(normal))
        self.sub(norm)
        return self

    def angle(self, other):
        """
        Returns the angle between this vector and the other
        """
        vect_a = math.sqrt(self.x**2 + self.y**2)
        vect_b = math.sqrt(math.pow(other.x, 2) + math.pow(other.y, 2))
        return math.acos((self.x*other.x+self.y*other.y)/(vect_a*vect_b))

    def draw(self, canvas, pt, clr):
        """
        Draw the vector from a particular point
        """
        canvas.draw_line(pt, (pt[0]+self.x, pt[1]+self.y), 1, clr)
