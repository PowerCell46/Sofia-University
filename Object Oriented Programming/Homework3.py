import math
from random import randint


class Point:
    def __init__(self, name=str, x=float, y=float):
        self._name = None
        self.name = name
        self._X = None
        self.X = x
        self._Y = None
        self.Y = y

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) == 1:
            if value.isalpha():
                self._name = value.upper()
            else:
                self._name = None
        else:
            self._name = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, value):
        if f'{value}'.isdigit():
            self._X = float(value)
        else:
            print('Invalid X - setting it to the default value of 0')
            self._X = 0

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, value):
        if f'{value}'.isdigit():
            self._Y = float(value)
        else:
            print('Invalid Y - setting it to the default value of 0')
            self._Y = 0

    def __str__(self):
        return f'Point {self.name} with Coordinates: X: {self.X:.2f}, Y: {self.Y:.2f}.'


# p = Point('m', 5, 10)
# print(p)


class Line:
    def __init__(self, first_point: Point, second_point: Point):
        if not isinstance(first_point, Point):
            first_point = Point('a', 0, 0)
        if not isinstance(second_point, Point):
            second_point = Point('b', 1, 1)

        if first_point is second_point:
            raise ValueError("The points cannot be the same!")

        if first_point.name == second_point.name:
            first_point.name = chr(randint(65, 90))

        self.first_point = first_point
        self.second_point = second_point
        self.name = f'{first_point.name}{second_point.name}'

    def distance(self):
        x1, y1 = self.first_point.X, self.first_point.Y
        x2, y2 = self.second_point.X, self.second_point.Y
        return f'The distance between {self.first_point.name} and {self.second_point.name} is: {math.sqrt((x2 - x1)**2 + (y2 - y1)**2)}'

    def __str__(self):
        return f'First Point {self.first_point.name} with Coordinates: X: {self.first_point.X}, Y: {self.first_point.Y}.\nSecond Point {self.second_point.name} with Coordinates: X: {self.second_point.X}, Y: {self.second_point.Y}.'


# i = Point('t', 10, 5)
# print(i)
#
# piLine = Line(p, i)
# print(piLine.distance())
# print(piLine)
