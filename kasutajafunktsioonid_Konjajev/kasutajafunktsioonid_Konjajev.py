from modul1 import *
from math import *

#7
kuupaev=date_(int(input("Kuupäev: ")),int(input("Kuu: ")),int(input("Aasta: ")))
print(kuupaev)


#6
a=is_prime(int(input("Kirjuta arv 0-1000: ")))
print(a)


#5
a=bank(int(input("Millist panust sa teha tahad?: ")))
years=bank(int(input("Kui kauaks?: ")))
print(bank(a,years))

#4
v=season(int(input("Kirjutage kuu number: ")))
print(v)


#3
v=square(int(input("Anna ruudu pikkus: ")))
print(v)


#2
aasta=is_year_leap(int(input("aasta:")))
print(aasta)


#1
v=arithmetic(float(input("a:")),input("c:"),float(input("b:")))
print(v)

