from math import sqrt, pi


class Line():
    def __init__(self, coords_1, coords_2):
        self.coords_1 = coords_1
        self.coords_2 = coords_2
        self.diffs = {
            'x': self.coords_1[0] - self.coords_2[0],
            'y': self.coords_1[1] - self.coords_2[1]
        }

    def distance(self):
        return round(
            sqrt((self.diffs.get('x')**2) + (self.diffs.get('y')**2)), 2)

    def slope(self):
        return round(self.diffs.get('y') / self.diffs.get('x'), 2)


c1 = (1, 8)
c2 = (8, 10)

line = Line(c1, c2)

print(line.slope())
print(line.distance())


## Cylinder
class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return round(pi * (self.radius**2) * self.height, 2)

    def surface_area(self):
        return round(((2 * pi) * self.radius * self.height) +
                     (2 * pi * (self.radius**2)), 2)


cylinder = Cylinder(2, 3)

print(cylinder.volume())
print(cylinder.surface_area())
