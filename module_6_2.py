# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.
# Задача "Изменять нельзя получать":

class Vehicle: # это любой транспорт
    __COLOR_VARIANTS = ["red", "blue","black", "white", "green"]

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner # владелец транспорта
        self.__model = __model # модель (марка) транспорта
        self.__engine_power = __engine_power # мощность двигателя
        self.__color = __color # название цвета

    def get_model(self,):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print("\033[34m", self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"\033[35m Нельзя сменить цвет на {new_color}.")

class Sedan(Vehicle): # седан
        __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedor', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
