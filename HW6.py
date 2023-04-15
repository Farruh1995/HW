# 1. дан словарь. создать новый словарь, поменяв ключ и значение местами.
#словарь
dist = {1 : '12', 2 : 'hga', 3 : '1pq2'}

dist2 = {x:i for i, v in dist.items()}

print(dist)
print(dist2)

#2. Написать программу для нахождения факториала.

n = int(input('Введите число: '))
def factirial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factirial_recursive(n-1)
print(factirial_recursive(n))

#3. Дан список чисел. Посчитать сколько раз встречается каждое число.


a = [1, 2, 4, 6, 4, 2, 1, 6, 7, 5, 6, 4, 2, 1]
b = {}
for povtor in a:
    b[povtor] = b.get(povtor, 0) + 1

d = {element: count for element, count in b.items() if count > 1}

print(d)


