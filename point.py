import random

class Point:
    def __init__(self, x, y):
        """
        Initialise a point object
        :param x: x-axis
        :param y: y-axis
        """
        self.x = x # Define x attribute via self.x and assigns the value x to it
        self.y = y # ""     y     ""        self.y

    def __str__(self):
        """
        Magic method that is called when we try to print an instantiate
        :return: [x, y]
        """
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        """
        Return the official string representation of the Point object.
        :return: A string representation identical to __str__
        """
        return self.__str__() # Use the same way of printing as 'str'

    def distance_orig(self):
        """
        Calculate the distance of the point from the origin (x = 0, y = 0)
        :return: distance from point
        """
        return (self.x**2 + self.y**2)**0.5  # Sqrt of the sum of x

    def __gt__(self, other):
        """
        Compare two points based on their distance
        :param other: other point to compare with
        :return: True if the point is farther away from the other point
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Compare two points on their distance from the origin
        :param other: other point to compare with
        :return: True if the points have the same distance from the origin
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

# Now we use points:
p = Point(1, 2) # P is an instance of 1 and 2
p_2 = Point(4.4, 50)

print(f"p.x = {p.x} and p.y = {p.y}") # Prints the coordinates relative to what has be selected
print(f"p_2.x = {p_2.x} and p_2.y = {p_2.y}")

print(p)

# Create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), random.randint(-10, 10))) # First randint is for x while the second for y

print("I got these 5 random points: ")
for p in points:
    print(p)

p = Point(3, 4)
print(p.distance_orig()) # Expect 5 answers

p_2 = Point(1, 1)
print(f"I am comparing p > p_2: {p>p_2}") # I expect to have true

print("The sorted list of point is:")
points.sort()
print(points)
