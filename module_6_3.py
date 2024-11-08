# Домашнее задание по теме "Множественное наследование"
# Цель: закрепить знания множественного наследования в Python.
# Задача "Ошибка эволюции"
import random

class Animal: # класс описывающий животных
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа
    x = 0
    y = 0
    z = 0
    _cards = [x, y, z] # координаты в пространстве

    def __init__(self, speed: int):

        self.speed = speed # скорость передвижения существа

    def move(self, dx, dy, dz): # перемещение
        if dz * self.speed<0:
            print("It's too deep, i can't dive :(")
        else:
            Animal.x = dx * self.speed
            Animal.y = dy * self.speed
            Animal.z = dz * self.speed

    def get_cords(self): # вывод координат
        print(f"X: {Animal.x}, Y: {Animal.y}, Z: {Animal.z}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True # наличие клюва
    def lay_eggs(self):
        random_number = random.randint(1, 4)
        print(f"Here are(is) {random_number} eggs for you")

class AquaticAnimal(Animal): # класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # перемещение с учетом скорости
        Animal.z=(Animal.z / 2) - abs(dz)

class PoisonousAnimal(Animal): # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal): # класс описывающий утконоса
    sound = "Click-click-click"

print(Duckbill.mro())
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
