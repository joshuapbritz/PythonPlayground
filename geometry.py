'''
Geometry module for working with shapes
'''
from math import sqrt, pi


class Line():
    '''
    A Class for working with lines
    '''

    def __init__(self, coords_1, coords_2):
        self.coords_1 = coords_1
        self.coords_2 = coords_2
        self.diffs = {
            'x': self.coords_1[0] - self.coords_2[0],
            'y': self.coords_1[1] - self.coords_2[1]
        }

    def distance(self):
        '''
        Get the distance between two points
        '''
        return round(
            sqrt((self.diffs.get('x')**2) + (self.diffs.get('y')**2)), 2)

    def slope(self):
        '''
        Get the slope of a line
        '''
        return round(self.diffs.get('y') / self.diffs.get('x'), 2)


## Cylinder
class Cylinder():
    '''
    A clas for working with cylinders
    '''

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        '''
        Get the voume of the cylinder
        '''
        return round(pi * (self.radius**2) * self.height, 2)

    def surface_area(self):
        '''
        Get the surface area of the cylinder
        '''
        return round(((2 * pi) * self.radius * self.height) +
                     (2 * pi * (self.radius**2)), 2)


class Circle():
    '''
    A Class for working with circles
    '''

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        '''
        Get the circumference of the circle
        '''
        return round(2 * pi * self.radius, 2)

    def get_area(self):
        '''
        Get the area of the circle
        '''
        return round(pi * (self.radius * self.radius), 2)

    def get_diameter(self):
        '''
        Get the diameter of the circle
        '''
        return self.radius * 2


class Square():
    '''
    A Class for working with squares
    '''

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)