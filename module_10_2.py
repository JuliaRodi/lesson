import time
from threading import Thread

class Knight(Thread):

    def __init__(self, name:str, power:int):

        Thread.__init__(self)
        self.enemies_count = 100
        self.name = name
        self.power = power
        self.days_to_fighting = self.enemies_count // power

    def run(self):
        print(f'{self.name}, на нас напали!')
        for day in range(self.days_to_fighting):
            time.sleep(1)
            enemies_keep = self.enemies_count - self.power * (day + 1)
            print(f'{self.name} сражается {day + 1} день(дня), осталось {enemies_keep} врагов \n')
            if enemies_keep == 0:
                print(f'{self.name} одержал победу спустя {day + 1} дней(день/дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


print('Все битвы закончились!')
