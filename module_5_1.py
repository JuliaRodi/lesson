class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'В доме "{self.name}" этажа №{new_floor} не существует.')
        else:
            for i in range(1, new_floor + 1):
                print(f' "{self.name}", вы находитесь на {i} этаже')

# Модуль 5_2
    def __len__ (self):
        return self.number_of_floors

    def __str__(self):
        return f'"Название: "{self.name}", кол-во этажей: {self.number_of_floors}"'

# Модуль 5_3
    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + int(value)

    def __radd__(self, value):
        return  int(value) + self.number_of_floors

    def __iadd__(self, value):
        return self.number_of_floors == self.number_of_floors + int(value)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h4 = House('ЖК ПИК', 10)
h5 = House('ЖК Акация', 20)

h1.go_to(5)
h2.go_to(10)
h3.go_to(17)
h2.go_to(1)

print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
print(len(h5))

print(str(h1))
print(str(h2))
print(str(h3))
print(str(h4))
print(str(h5))

print(h4 == h5) # __eq__

h4 = h4 + 10 # __add__
print(h4)
print(h4 == h5)

h4 += 10 # __iadd__
print(h4)

h5 = 10 + h5 # __radd__
print(h5)

print(h4 > h5) # __gt__
print(h4 >= h5) # __ge__
print(h4 < h5) # __lt__
print(h4 <= h5) # __le__
print(h4 != h5) # __ne__