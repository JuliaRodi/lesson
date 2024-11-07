# Домашнее задание по теме "Множественное наследование"
# Цель: закрепить знания множественного наследования в Python.
# Задача "Ошибка эволюции"
import random

class Animal: # класс описывающий животных
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, _cords, speed):
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа

    def move(self, dx, dy, dz): # перемещение
        _cords = self.speed[dx, dy, dz]
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return

    def get_cords(self): # вывод координат
        print(f"X: {self.dx}, Y: {self.dy}, Z: {self.dz}")

    def attack(self):
        i = 10
        if i in self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif i in self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True # наличие клюва
    def lay_eggs(self):
        print(f"Here are(is) {random.randint (0, 4)} eggs for you")

class AquaticAnimal(Animal): # класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.dz = abs(dz)
        _cords = self.speed[dx, dy, dz-2]
        self.dz - 2

class PoisonousAnimal(Animal): # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal): # класс описывающий утконоса
    sound = "Click-click-click"
    # def __init__(self, sound: str, beak, _DEGREE_OF_DANGER, move, get_cords, dive_in, lay_eggs):
    #     self.sound = "Click-click-click"
    #     super().__init__(beak, _DEGREE_OF_DANGER, move, get_cords, dive_in, lay_eggs)

print(Duckbill.mro())
db = Duckbill(10)

print(db.live)
print(db.beak)

db.sound()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()