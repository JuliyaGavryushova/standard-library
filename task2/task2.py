"""Взять любую задачу и настроить в ней запуск скрипта с параметрами.
(используем Пайчарм и модуль argparse)"""


class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width, height=None):

        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self.width = width
        if height is None:
            self.height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self.height = height

    @property
    def width(self):

        return self._width

    @width.setter
    def width(self, value):

        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):

        return self._height

    @height.setter
    def height(self, value):

        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):

        return 2 * (self.width + self.height)

    def area(self):

        return self.width * self.height

    def __add__(self, other):

        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):

        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):

        return self.area() < other.area()

    def __eq__(self, other):

        return self.area() == other.area()

    def __le__(self, other):

        return self.area() <= other.area()

    def __str__(self):

        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):

        return f"Rectangle({self.width}, {self.height})"


# r = Rectangle(5, 2)
# print(r.__str__())