from modul1 import *
from math import *

#7
day=date(int(input("�������� ����: ")))
mounth=date(int(input("�������� �����: ")))
year=date(int(input("�������� ���: ")))
print(date(day,mounth,year))

#6
a=is_prime(int(input("�������� ����� �� 0-1000: ")))
print(a)
#5

a=bank(int(input("����� ����� �� ������ ��������: ")),)
years=bank(int(input("�� ������� ���: ")))
print(bank(a,years))

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

