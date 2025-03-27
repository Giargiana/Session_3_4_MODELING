from color_point import Colorpoint

class AdvancedPoint(Colorpoint):
    """
    Class with additional functionality
    """
    COLORS = ['red', 'blue', 'green', 'yellow', 'black']
    def __init__(self, x, y, color):
        """
        Creates an object with x and y coordinates, wiht a determined color. It raises point exception if the color is not in the list 'COLORS'
        :param x: x-coordinates
        :param y: y-coordinates
        :param color: color of the point
        """
        if color not in self.COLORS:
            raise PointException(f'Invalid color, must be one of {self.COLORS}')
        super().__init__(x, y, color)

    @classmethod
    def add_color(cls, color):
        """
        Add color to the COLOR list
        :param color: color to be added
        :return: new color to the list 'COLOR'
        """
        cls. COLORS.append('rojo')

    @staticmethod
    def from_tuple(coordinate, color = 'red'):
        """
        Create object from a tuple of coordinates
        :param coordinate: tuple coordinates
        :param color: color of the point
        :return: istance of 'AdvancedPoint'
        """
        x, y = coordinate
        return AdvancedPoint (x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate distance between the two points
        :param p1: point 1
        :param p2: point 2
        :return: distance between points
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculate distance between 'AdvancedPoint and other point
        :param p: other object
        :return: distance among the two points
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

AdvancedPoint.add_color('rojo')

p = AdvancedPoint(1, 2, 'rojo')
print(p)
print(p.distance_orig())

p_2 = AdvancedPoint.from_tuple((3, 2))
print(p_2)

print(AdvancedPoint.distance_2_points(p, p_2))
print(p.distance_to_other(p_2))

