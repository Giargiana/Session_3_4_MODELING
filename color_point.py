from point import Point
import random

class Colorpoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)): # Wont plug in values that are not numbers
                raise TypeError ('X must be a number')
        if not isinstance(y, (int, float)): # Wont plug in values that are not numbers
                raise TypeError ('Y must be a number')

        super().__init__(x, y) # Replaces the self.x and self.y
        self.color = color

    def __str__(self):
        return f"[{self.color}: {self.x}, {self.y}]"

p = Colorpoint(1, 2, "red")

print(p.distance_orig())

print(p)


# colors = ["red", 'green', 'yellow', 'black', 'magenta', 'cyan', 'white', 'marsala']
#
# color_points = []
#
# for i in range(10):
#     color_points.append(Colorpoint(random.randint(-10, 10), random.randint(-10, 10), random.choice(colors)))
#
# print(color_points)
# color_points.sort()
#
# print(color_points)