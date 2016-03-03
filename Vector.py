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
        self.x_coord = p[0]
        self.y_coord = p[1]

    # Returns a string representation of the vector
    @property
    def __str__(self):
        """
        Returns the coords as a tupled string
        """
        return "(" + str(self.x_coord) + "," + str(self.y_coord) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        """
        Check if this vector=other
        """
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

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
        return self.x_coord, self.y_coord

    # Returns a copy of the vector
    def copy(self):
        """
        Copy the vector and return it
        """
        vct = Vector()
        vct.x_coord = self.x_coord
        vct.y_coord = self.y_coord
        return vct

    # Multiplies the vector by a scalar
    def mult(self, k):
        """
        Semi scalar product
        """
        self.x_coord *= k
        self.y_coord *= k
        return self

    # Divides the vector by a scalar
    def div(self, k):
        """
        Semi scalar division
        """
        self.x_coord /= k
        self.y_coord /= k
        return self

    # Normalizes the vector
    def normalise(self):
        """
        Normalization
        """
        vct = math.sqrt(self.x_coord**2 + self.y_coord**2)
        self.x_coord /= vct
        self.y_coord /= vct

    # Returns a normalized version of the vector
    @property
    def get_normalised(self):
        """
        get the normalised coords
        """
        return [self.x_coord / math.sqrt(math.pow(self.x_coord, 2) + math.pow(self.y_coord, 2)),
                self.y_coord / math.sqrt(math.pow(self.x_coord, 2) + math.pow(self.y_coord, 2))]

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
        self.x_coord += other.x_coord
        self.y_coord += other.y_coord
        return self

    # Subtracts another vector from this vector
    def sub(self, other):
        """
        Vector substraction
        """
        self.x_coord -= other.x_coord
        self.y_coord -= other.y_coord
        return self

    # Returns the zero vector
    def zero(self):
        """
        Reset
        """
        self.x_coord = 0
        self.y_coord = 0
        return self

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        """
        Negation
        """
        self.x_coord = -self.x_coord
        self.y_coord = -self.y_coord
        return self

    # Returns the dot product of this vector with another one
    def dot(self, other):
        """
        Scalar product
        """
        return self.x_coord*other.x_coord + self.y_coord*other.y_coord

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
        return self.x_coord**2 + self.y_coord**2

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
        vect_a = math.sqrt(self.x_coord**2 + self.y_coord**2)
        vect_b = math.sqrt(math.pow(other.x_coord, 2) + math.pow(other.y_coord, 2))
        return math.acos((self.x_coord*other.x_coord+self.y_coord*other.y_coord)/(vect_a*vect_b))

def docstring():
    """
    Document string
    """
    #print("The module that implements vectors.")
    return "The module that implements vectors."
