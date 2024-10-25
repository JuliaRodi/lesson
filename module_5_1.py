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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)

h1.go_to(5)
h2.go_to(10)
h3.go_to(17)
h2.go_to(1)