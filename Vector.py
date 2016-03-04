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

    # Returns a string representation of the vector
    @property
    def __str__(self):
        """
        Returns the coords as a tupled string
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        """
        Check if this vector=other
        """
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        """
        Check if this vector!=other
        """
        return not self.__eq__(other)

    # Returns a tuple with the point corresponding to the vector
    def get_pt(self):
        """
        Get the coords
        """
        return (self.x, self.y)

    # Returns a copy of the vector
    def copy(self):
        """
        Copy the vector and return it
        """
        vct = Vector()
        vct.x = self.x
        vct.y = self.y
        return vct

    # Multiplies the vector by a scalar
    def mult(self, k):
        """
        Semi scalar product
        """
        self.x *= k
        self.y *= k
        return self

    # Divides the vector by a scalar
    def div(self, k):
        """
        Semi scalar division
        """
        self.x /= k
        self.y /= k
        return self

    # Normalizes the vector
    def normalise(self):
        """
        Normalization
        """
        vct = math.sqrt(self.x**2 + self.y**2)
        self.x /= vct
        self.y /= vct

    # Returns a normalized version of the vector
    @property
    def get_normalised(self):
        """
        get the normalised coords
        """
        return [self.x / math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)),
                self.y / math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))]

    # Returns the normal of that vector
    @property
    def get_normal(self):
        """
        Get the normal of the vector
        """
        return Vector(self.get_normalised)

    # Adds another vector to this vector
    def add(self, other):
        """
        Vector addition
        """
        self.x += other.x
        self.y += other.y
        return self

    # Subtracts another vector from this vector
    def sub(self, other):
        """
        Vector substraction
        """
        self.x -= other.x
        self.y -= other.y
        return self

    # Returns the zero vector
    def zero(self):
        """
        Reset
        """
        self.x = 0
        self.y = 0
        return self

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        """
        Negation
        """
        self.x = -self.x
        self.y = -self.y
        return self

    # Returns the dot product of this vector with another one
    def dot(self, other):
        """
        Scalar product
        """
        return self.x*other.x + self.y*other.y

    # Returns the length of the vector
    def length(self):
        """
        Size
        """
        return math.sqrt(self.length_sq())

    # Returns the squared length of the vector
    def length_sq(self):
        """
        Size^2
        """
        return self.x**2 + self.y**2

    # Reflect this vector on a normal
    def reflect(self, normal):
        """
        Reflection
        """
        norm = normal.copy
        norm.mult(2*self.dot(normal))
        self.sub(norm)
        return self

    # Returns the angle between this vector and another one
    def angle(self, other):
        """
        Get the angle between this vector and the other
        """
        vect_a = math.sqrt(self.x**2 + self.y**2)
        vect_b = math.sqrt(math.pow(other.x, 2) + math.pow(other.y, 2))
        return math.acos((self.x*other.x+self.y*other.y)/(vect_a*vect_b))
