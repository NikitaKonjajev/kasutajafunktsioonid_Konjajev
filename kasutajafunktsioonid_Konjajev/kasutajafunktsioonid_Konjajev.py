from modul1 import *
from math import *
#5


#4
v=season(int(input("������� ����� ������� ����: ")))
print(v)

#3
v=square(int(input("������� ������: ")))
print(v)

#2
aasta=is_year_leap(int(input("aasta:")))
print(aasta)


#1
v=arithmetic(float(input("a:")),input("c:"),float(input("b:")))
print(v)

def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
    return a