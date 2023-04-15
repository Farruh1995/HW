#Task 7_1
# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
#Task 7_2
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
# while True:
#     menu = int(input("Что бы конвертировать ведите порядковый номер ))
#     if menu == 1:
#         inch_sm()
#     elif menu == 2:
#         sm_inch()
#     elif menu == 3:
#         mil_cm()
#     elif menu == 4:
#         cm_mil()
#     elif menu == 5:
#         lb_kg()
#     elif menu == 6:
#         kg_ld()
#     elif menu == 7:
#         oz_gr()
#     elif menu == 8:
#         gr_oz()
#     elif menu == 9:
#         gal_lit()
#     elif menu == 10:
#         lit_gal()
#     elif menu == 11:
#         pin_lit()
#     elif menu == 12:
#         lit_pim()
def inch_sm():
    sm = float(input("Введите дюймы: ")) * 2.54
    print(sm)

def sm_inch():
    inch = float(input("Введите сантиметры: ")) / 2.54
    print(inch)


def mil_cm():
    cm = float(input("Введите мили: ")) * 1.60934
    print(cm)


def cm_mil():
    mil =float(input("Введите километры: ")) / 1.60934
    print(mil)

def lb_kg():
    kg = float(input("Введите фунты: ")) * 0.453592
    print(kg)
def kg_lb():
    lb = float(input("Введите килограммы: ")) / 0.453592
    print(lb)

def oz_gr():
    gr = float(input("Введите унции: ")) * 28.3495
    print(gr)


def gr_oz():
    oz = float(input("Введите граммы: ")) / 28.3495
    print(oz)


def gal_lit():
    lit = float(input("Введите галлоны: ")) * 4.54609
    print(lit)

def lit_gal():
    gal = float(input("Введите литры: ")) / 4.54609
    print(gal)

def pin_lit():
    lit = float(input("Введите пинты: ")) * 0.568261
    print(lit)

def lit_pin():
    pin = float(input("Введите литры: ")) / 0.568261
    print(pin)


while True:
    menu = float(input(
        'Что бы конвертировать введите номер из списка, где: \n 1. Дюймы в сантиметры \n 2. Сантиметры в дюймы \n 3. Мили в километры \n 4. Километры в мили \n 5. Фунты в килограммы \n 6. Килограммы в фунты \n 7. Унции в граммы \n 8. Граммы в унции \n 9. Галлон в литры \n 10. Литры в галлоны \n 11. Пинты в литры \n 12. Литры в пинты \n 0. Выход с программы. \0 Укажите номер: '))

    if menu == 1:
        inch_sm()
    elif menu == 2:
        sm_inch()
    elif menu == 3:
        mil_cm()
    elif menu == 4:
        cm_mil()
    elif menu == 5:
        lb_kg()
    elif menu == 6:
        kg_ld()
    elif menu == 7:
        oz_gr()
    elif menu == 8:
        gr_oz()
    elif menu == 9:
        gal_lit()
    elif menu == 10:
        lit_gal()
    elif menu == 11:
        pin_lit()
    elif menu == 12:
        lit_pim()

