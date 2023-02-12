from modul1 import *
from math import *

#7
day=date(int(input("Напишете день: ")))
mounth=date(int(input("Напишете месяц: ")))
year=date(int(input("Напишете год: ")))
print(date(day,mounth,year))

#6
a=is_prime(int(input("Напишите число от 0-1000: ")))
print(a)
#5

a=bank(int(input("скоко денег вы хотите положить: ")),)
years=bank(int(input("На сколько лет: ")))
print(bank(a,years))

#4
v=season(int(input("Введите цефру времени года: ")))
print(v)

#3
v=square(int(input("Введите длинну: ")))
print(v)

#2
aasta=is_year_leap(int(input("aasta:")))
print(aasta)


#1
v=arithmetic(float(input("a:")),input("c:"),float(input("b:")))
print(v)

