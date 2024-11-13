import math

class Figure:
    sides_count = 0
    def __init__(self, sides: list, color: list, filled = False):
        self.__sides = sides # список сторон
        self.__color = color # список цветов в формате RGB
        self.filled = filled # заливка

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if all(0 <= value <= 255 and isinstance (value, int) for value in [r, g, b]):
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count and all(isinstance(i, (int)) and i > 0 for i in args):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    __radius = None

    def __init__(self, color: list, radius, filled = False):
        super().__init__(color, radius, filled = filled)

    def get_square(self):
        radius = self.get_sides()[0]  # Получаем радиус из сторон
        return math.pi * (radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, sides: list, filled = False):
        super().__init__(color, sides, filled = filled)

    def get_square(self):
        p = self.__len__() / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, side_length = 1, filled = False):
        sides = [side_length] * 12
        super().__init__(color, sides, filled = filled)

    def get_volume(self):
        side_length = self.get_sides()[0]  # Получаем длину стороны
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
