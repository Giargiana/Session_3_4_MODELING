from color_point import Colorpoint

class AdvancedPoint(Colorpoint):
    COLORS = ['red', 'blue', 'green', 'yellow', 'black']
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise PointException(f'Invalid color, must be one of {self.COLORS}')
        super().__init__(x, y, color)

    @classmethod
    def add_color(cls, color):
        cls. COLORS.append('rojo')

    @staticmethod
    def from_tuple(coordinate, color = 'red'):
        x, y = coordinate
        return AdvancedPoint (x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

AdvancedPoint.add_color('rojo')

p = AdvancedPoint(1, 2, 'rojo')
print(p)
print(p.distance_orig())

p_2 = AdvancedPoint.from_tuple((3, 2))
print(p_2)

print(AdvancedPoint.distance_2_points(p, p_2))
print(p.distance_to_other(p_2))

