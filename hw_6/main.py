# Задание 1
from time import sleep


class TrafficLight:

    __color = {'красный': 7, 'желтый': 2, 'зелёный': 15}

    def running(self):
        while True:
            for i in TrafficLight.__color:
                print(i)
                sleep(TrafficLight.__color[i])


test_light = TrafficLight()
test_light.running()


# Задание 2

class Road:

    def __init__(self, length, width):

        if length > 0 and width > 0:
            self._length = length
            self._width = width
        else:
            raise ValueError("Один из атрибутов меньше или равен 0")



    def counter(self, weight, thickness):
        if weight == 0 or thickness == 0:
            raise ValueError("Один из атрибутов меньше или равен 0")
        else:
            return f'Масса асфальта: {self._length * self._width * weight * thickness} т'


a = Road(500, 20)
print(a.counter(25, 5))


# Задание 3

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f'Общий доход: {total_income} руб.'

a = Position('Иван', 'Иванов', 'охранник', {'wage': 30000, 'bonus': 10000})

print(a.get_full_name())
print(a.get_total_income())


# Задание 4
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.current_speed = 0

    def go(self):
        self.current_speed = randint(1, self.speed)
        return f'Машина поехала'

    def stop(self):
        self.current_speed = 0
        return f'Машина остановилась'

    def turn(self, direction):
        self.current_speed = randint(10, self.speed)
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.current_speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.current_speed > 60:
            return f'Превышение скорости. Текущая скорость: {self.current_speed} км/ч'
        else:
            return f'Текущая скорость: {self.current_speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.current_speed > 40:
            return f'Превышение скорости. Текущая скорость: {self.current_speed} км/ч'
        else:
            return f'Текущая скорость: {self.current_speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_highway_patrol, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.is_highway_patrol = is_highway_patrol

class SportCar(Car):
    def __init__(self, speed, color, name, acceleration_time, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.acceleration_time = acceleration_time

test_car_1 = TownCar(300, 'red', 'volvo', False)
print(test_car_1.go())
print(test_car_1.turn('налево'))
print(test_car_1.show_speed())
print('-----------------------')

test_car_2 = WorkCar(200, 'grey', 'lada', True)
print(test_car_2.go())
print(test_car_2.turn('направо'))
print(test_car_2.show_speed())
print('-----------------------')

test_car_3 = PoliceCar(300, 'blue', 'bmw', False)
print(test_car_3.go())
print(test_car_3.turn('направо'))
print(test_car_3.show_speed())


test_car_4 = SportCar(400, 'yellow', 'ferrari', 7)
print(test_car_4.go())
print(test_car_4.turn('направо'))
print(test_car_4.show_speed())

# Задание 5

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):

    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):

    def draw(self):
        return 'Запуск отрисовки маркером'


test_pen = Pen('Ручка')
print(test_pen.draw())

test_pencil = Pencil('Карандаш')
print(test_pencil.draw())

test_handle = Handle('Карандаш')
print(test_handle.draw())