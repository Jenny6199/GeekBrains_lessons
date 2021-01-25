""" Author: Maksim Sapunov msdir6199@gmail.com 23/01/2021"""


class Car:
    """ Общее представление автомобиля """

    _car_count = 0
    _is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        Car._car_count += 1

    def go(self):
        """ Метод инициирует движение автомобиля """
        print(f'Engine start, {self.name} is running')

    def stop(self):
        """ Метод для остановки автомобиля """
        print(f'{self.name} was stopped.')

    def turn(self, direction):
        """ Метод для поворота в указанную сторону """
        print(f'{self.name}  turn to {direction}')

    def show_speed(self):
        """ Метод выводит информацию о скорости автомобиля """
        print(f'{self.name} - {self.speed}')

    def is_police(self):
        """ Метод проверяет - является ли автомобиль полицейской машиной """
        if self._is_police:
            print("Yes")
        else:
            print("No")

    @staticmethod
    def car_count():
        """ Метод выводит информацию о количестве созданных объектов класса автомобиль """
        print(Car._car_count)


class TownCar(Car):
    """ Общая модель представления автобуса """

    def __init__(self, speed, color, name, capacity=40):
        super().__init__(speed, color, name)
        self.capacity = capacity

    def show_capacity(self):
        """ Метод позволяющий вывессти информацию о вместимости автобуса """
        print(f' {self.name} can get {self.capacity} passengers')

    def show_speed(self):
        """ Метод позволяющий вывести информацию о скорости автобуса """
        print(f' {self.name} speed is {self.speed} km per hour')
        if self.speed > 60:
            print(f'{self.name} need to reduce his own speed to 60!')


class SportCar(Car):
    """ Общая модель представления спортивного автомобиля """

    def __init__(self, speed, color, name, acceleration=3):
        super().__init__(speed, color, name)
        self.acceleration = acceleration

    def increase_speed(self):
        """ Метод инициирующий разгон спортивного автомобиля """
        self.speed *= self.acceleration
        print(f'{self.name} accelerate to {self.speed} km per hour\nHis very fast!')


class WorkCar(Car):
    """ Общая модель представления грузового автомобиля """

    def __init__(self, speed, color, name, cargo='Empty'):
        super().__init__(speed, color, name)
        self.cargo = cargo

    def show_speed(self):
        """ Метод позволяет получить информацию о скорости движения грузовика """
        print(f'{self.name}  speed is {self.speed}')
        if self.speed > 40:
            print(f'{self.name}  need to reduce  his own speed!')

    def get_cargo(self):
        """ Метод инициирует погрузку грузовика """
        self.cargo = 'Full'
        print('Cargo full')

    def out_cargo(self):
        """ Метод инициирует разгрузку грузовика """
        self.cargo = 'Empty'
        print('Cargo empty')


class PoliceCar(Car):
    """ Общая модель представления полицейского автомобиля """

    def __init__(self, speed, color, name, board_number):
        super().__init__(speed, color, name)
        self.board_number = board_number
        self._is_police = True

    def alarm(self):
        """ Метод включения полицейской сирены """

        if self._is_police:
            print(f'\033[31mThis is police!\033[0m {self.board_number}')


a1 = PoliceCar(90, 'blue', 'Toyota', '011')
a1.alarm()
a1.go()

a2 = WorkCar(70, 'red', 'Man', 'Empty')
a2.get_cargo()
a2.show_speed()

a3 = SportCar(100, 'white', 'Lamborghini')
a3.go()
a3.increase_speed()

a3.is_police()
a3.car_count()
