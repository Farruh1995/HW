from copy import copy, deepcopy
from math import sqrt
# task 1.1
a = float(input('a = '))
b = float(input('b = '))
print('Сумма данных чисел=', a+b)
print('Разность данных чисел=', a-b)
print('Произведение данных чисел=', a*b)
#task 1.2
x = int(input('Введите первое число x: '))
y = int(input('Введите второе число у: '))
print((abs(x)-abs(y))/(1+abs(x*y)))
#task 1.3
a = int(input('Введите длину ребра '))
print('Объем равен ' + str(a ** 3))
print('Площадь боковой поверхности равна ' + str(a * a * 4))
#task 1.4
a=int(input('Введите первое число:' ))
b=int(input('Введите второе число:' ))
sa=(a+b)/2
import math
sg=math.sqrt(a*b)
print('Среднее арифметическое:',sa)
print('Среднее геометрическое:',sg)
#task 1.5
a = int(input('Введите первый катет: '))
b = int(input('Введите второй катет: '))
import math
c = math.sqrt(a*a+b*b)
p=(a*b*c)/2
print('Гипотенуза:',c)
print('Площадь:',p)
