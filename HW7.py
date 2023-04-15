# 1.Написать декоратор, который будет выводить время выполнения
# функции, а также аргументы, с которыми она была вызвана.
import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("111", "0000"))

#2. Написать программу, которая проверяет, начинается ли строка с
#данного символа, используя lambda функцию.

simvol = 'w'
while True:
    line = input('Введите символы: ')
    a = lambda simvol, line: 'Ваш текст начинается с заданного символа' if simvol == line[0] else 'Совпадения в первом символе не найдено.'
    print(a(simvol, line))
    break#Даниил, как здесь правильно закольцевать ?
# 3. Написать программу, которая проверяет, является ли данная строка
# числом или нет, используя lambda функцию.

lin = input('Введите символы: ')
b = lambda lin: 'Ваш символ-число.' if lin.isdigit() else 'Нет числа.'
print(b(lin))
#4.  Написать программу, которая ищет числа, делящиеся на 19 или 13 в списке чисел, используя lambda функцию.
li = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
b = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), li))
print(b)











