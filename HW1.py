from copy import copy, deepcopy
from math import sqrt
# task_2_1
a = 50
b = a
c = b
print(a)
print(b)
print(c)
print(id(a), id(b), id(c))
# task_2_2
d = [1, 2, 3]
e = copy(d)
print(d)
print(e)
print(id(d), id(e))
# task_2_3
a = str(a)
b = str(b)
c = str(c)
d = tuple(d)
e = d
print(a)
print(b)
print(c)
print(d)
print(e)
print(id(a), id(b),id(c),id(d),id(e))
# task_2_4 - я так и не понял как делать.
input()
a = int()
b = int()
