# Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
# переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран. Перегрузить
# конструктор на обработку входных параметров вида: одна строка, три
# числа, другой объект класса MyTime, и отсутствие входных параметров.


class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if isinstance(hours, str):
            time_str = hours.split(":")
            self.hours = int(time_str[0])
            self.minutes = int(time_str[1])
            self.seconds = int(time_str[2])
        elif isinstance(hours, MyTime):
            self.hours = hours.hours
            self.minutes = hours.minutes
            self.seconds = hours.seconds
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return MyTime.from_seconds(total_seconds)

    def __sub__(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return MyTime.from_seconds(total_seconds)

    def __mul__(self, other):
        total_seconds = self.to_seconds() * other
        return MyTime.from_seconds(total_seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return MyTime(hours, minutes, seconds)


t1 = MyTime(10, 30, 0)
t2 = MyTime("12:45:15")
t3 = MyTime(t1)
t4 = MyTime()

print(t1)
print(t2)
print(t1 + t2)
print(t1 - t2)
print(t1 * 2)
print(t1 == t3)
print(t1 != t2)


