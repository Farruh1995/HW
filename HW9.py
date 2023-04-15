#1. Создать пять классов описывающие реальные объекты. Каждый класс
#должен содержать минимум три приватных атрибута, конструктор, геттеры
#и сеттеры для каждого атрибута, два метода.

class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def greet(self):
        print(f"Hello, my name is {self.__name}")

    def introduce(self):
        print(f"My name is {self.__name}, I am {self.__age} years old and {self.__height} cm tall")


class Auto:
    def __init__(self, model, color, age):
        self.__model = model
        self.__color = color
        self.__age = age

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def description(self):
        print(f'model: {self.__model}, color: {self.__color}, age: {self.__age}')

    def praise(self):
        print(f'{self.__model} is cool car')


class Food:
    def __init__(self, name, weight, carb):
        self.__name = name
        self.__weight = weight
        self.__carb = carb

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_carb(self):
        return self.__carb

    def set_carb(self, carb):
        self.__carb = carb

    def chek_carb(self):
        if self.__carb >= 100:
            print('this food contains a lot of carbohydrates')
        else:
            print('this food is low in carbohydrates')

    def menu(self):
        print(f'on the menu today {self.__name}, weighs: {self.__weight}gr, contains carbohydrates: {self.__carb}')


class Phone:
    def __init__(self, model, foo, id):
        self.__model = model
        self.__foo = foo
        self.__id = id

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_foo(self):
        return self.__model

    def set_foo(self, foo):
        self.__foo = foo

    def get_number(self):
        return self.__id

    def set_number(self, id):
        self.__id = id

    def phone_foo(self):
        print(f'{self.__model} - the phone has functions: {self.__foo}')

    def phone_id(self):
        print(f'this phone has id: {self.__id}')


class Beer:
    def __init__(self, brand, alk, ml):
        self.__brand = brand
        self.__alk = alk
        self.__ml = ml

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_alk(self):
        return self.__alk

    def set_alk(self, alk):
        self.__alk = alk

    def get_ml(self):
        return self.__ml

    def set_ml(self, ml):
        self.__ml = ml

    def beer_brand(self):
        print(f'this beer {self.__brand}')

    def beer_alk(self):
        if self.__alk > 5:
            print('this beer is strong')
        else:
            print('this beer is not strong')


a = Beer('pilsner', 4.1, 0.5)
a.beer_alk()
#Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
#умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
#скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
#разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, m, mod, y, s=0):
        self.__brand = m
        self.__model = mod
        self.__year = y
        self.__speed = s

    def plus_speed(self):
        self.__speed += 5

    def min_speed(self):
        self.__speed -= 5

    def stop_speed(self):
        self.__speed = 0

    def pr_speed(self):
        return self.__speed

    def reverse(self):
        self.__speed = -self.__speed
        print(self.__speed)


car1 = Car('audi', 'a4', 2000, 60)

