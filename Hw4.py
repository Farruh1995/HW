#Task_4_1
#Поменять слова местами.через слип.
a = 'Anno'
b = 'Domini'
print(b+ ' ' +a)
# Добавить восклицательный знак в начало и конец
c = f'!{a} {b}!'
print(c)
#Слова разделить 3 символами
d = 'Anno {} Demini'.format('!')
print (d)
#Task_4-2-4-3
#Написать программу которая получит имя и возраст
#Вечный цикл
while True:
    name = input('Ваше имя: ')
    old = input('Ваш возраст: ')
    if not (old.isdigit()):
        print('Ошибка, повторите ввод.')
    elif old.isdigit():
        old = int(old)
        if 0 >= old:
            print('Ошибка, повторите ввод.')
        elif 0 < old < 10:
            print(f'Привет шкет {name}!')
        elif 10 < old < 18:
            print(f'Как дела, {name}?')
        elif 18 <= old < 100:
            print(f'Что желаете, {name}?' )
        else:
            print(f'{name} вы лжете-в нашей время столько не живут...')


