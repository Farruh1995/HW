# #1. Создать свой калькулятор
# # 2. Обернуть его в try/except
# def add(x, y):
#     return x+y
# def subtract(x, y):
#     return x-y
# def multiply(x, y):
#     return x*y
# def divide(x, y):
#     return x/y
#
# print("Выберите операцию.\n"
#       "1. Сложение.\n"
#       "2. Вычисление.\n"
#       "3. Умножение.\n"
#       "4. Деление.")
#
# try:
#     choice = input("Введите номер операции: ")
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     if choice == '1':
#         print(num1, "+", num2, "=", add(num1, num2))
#     elif choice == '2':
#         print(num1, "-", num2, "=", subtract(num1,num2))
#     elif choice == '3':
#         print(num1,"*", num2, "=", multiply(num1,num2))
#     elif choice == '4':
#         print(num1, "/", num2, "=", divide(num1,num2))
#
# except ValueError:
#     print("Некорректный ввод. Введите число.")
# except ZeroDivisionError:
#     print("Деление на ноль невозможно.")

#1.Создать генератор геометрической прогрессии
#2.Подключить дебаггинг
# import pdb
# def geometric_progression(start,
# conclusion):
#     pdb.set_trace()
#     while True:
#         yield start
#         start *= conclusion
#
# gp = geometric_progression(3, 7)
# print(next(gp))
# print(next(gp))
# print(next(gp))
# print(next(gp))
#1. Написать свой класс MyOpen, объекты которого должны поддерживать протокол контекстного менеджера. Он должен работать аналогично with open(‘file.txt’, ‘w+’) as f. Т.е вы можете применять его следующим образом:
#with MyOpen(file.txt’, ‘w+’) as f:
# class MyOpen:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return  self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

#2.Написать свой итератор(реализовать у него и метод __next__ и __iter__), чтобы при обходе циклом он отдавал только элементы на четных индексах, возведенные в квадрат.
# class EvenSquare:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.lst):
#             value = self.lst[self.index]
#             self.index += 1
#             if value % 2 == 0:
#                 return value**2
#         raise StopIteration
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for num in EvenSquare(lst):
#     print(num)

# 3. Написать генератор, который будет принимать на вход имя файла и генерировать построчно(т.е yield каждой строки).
def read_file(filename):
    with open(filename,'r') as f:
        for line in f:
            yield line.split()
    for line in read_file('example.txt'):
        print(line)

#4. Просмотреть ваше задание, где вы реализовывали класс Car и подумать, где стоит добавить выкидывание(raise) исключений(например, когда скорость может стать меньше 0). В месте, где вы работаете с этим классом , добавьте обработку этих исключений, используя конструкцию try.