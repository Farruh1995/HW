# 1. Декодировать в строку байтовое значение.
# a = b'r\xc3\xa9sum\xc3\xa9'
# b = a.decode("utf-8")
# print(b)
# c = b.encode("latin-1")
# print(c)
# d = c.decode("latin-1")
# print(d)
# 2. Ввести с клавиатуры 4 строки.

# str1 = input('Введите первую строку: ')
# str2 = input('Введите вторую строку: ')
# str3 = input('Введите третью строку: ')
# str4 = input('Ведите четвертую строку: ')
# f = open('text.txt', 'w')
# f.write(str1)
# f.write('\n')
# f.write(str2)
# f.write('\n')
# f.close()
# f = open('text.txt', 'a+')
# f.write(str3)
# f.write('\n')
# f.write(str4)
# f.close()

# 3.
import json

one = {234567: ["one", 1], 134567: ['two', 2 ], 124567: ['three', 3], 123567: ['four', 4], 123467: ['five', 5]}
with open ('one.txt.json', 'w') as write_file:
    json.dump(one, write_file)

#4. Я так и не смог сделать все условия задачи.

import csv

with open('one.txt.json') as write_file:
    one = json.load(write_file)
one["Phone"] = 123456
with open ('one.csv', 'w') as write_file:
    writer = csv.DictWriter(write_file, fieldnames=[123456,"\n",234567,"\n",134567,"\n",124567,"\n",123567,"\n",123467])
    writer.writeheader()








