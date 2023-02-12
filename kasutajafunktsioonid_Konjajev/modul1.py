from math import *
#7
def date(day,month,year:int):
    """
    """
    if day <= 0 or month <= 0 or year < 0:
        return False
    else:
        pass

#6
def is_prime(a):
    """
    """
    if a%a==0 and a!= 0:
        return True
    else:
        return False

#5
def bank(a,years:int):
    """
    """
    i=0
    while i<years:
        a=a+a*0.1
    i=i+1
    return a

#4
def season(n:int)->str:
    """
    """
    if n==12 or 1 <= n <=2:
        print("Talv")
    elif 3<= n <=5:
        print("Kevad")
    elif 6<= n <=8:
        print("Suvi")
    elif 9<= n <=11:
        print("Sügis")
    return n

#3
def square(a:float)->int:
   """
   """
   p=a*4
   s=a*a
   d=(a**2)/2
   return p,s,d

#2
def is_year_leap(aasta:int)->bool:
    """Aastat
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#1
def arithmetic(a:float,c:str,b:float)->any:
    """kalkulaator
    """
    if c=="+":
        v=a+b
    elif c=="-":
        v=a-b
    elif c=="*":
        v=a*b
    elif c=="/":
        if b==0:
            v="DIV0"
        else:
            v=a/b
    else:
        v="Неизвестная операция"
    return v



