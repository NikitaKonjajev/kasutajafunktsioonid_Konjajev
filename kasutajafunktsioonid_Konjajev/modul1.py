from math import *
from datetime import *

#7
def date_(d:int,m:int,y:int)->bool:
    """
    """
    try:
        print(date_(y,m,d))
        flag=True
    except:
        flag=False
    return flag
#6
def is_prime(a)->any:
    """
    """
    flag=True
    for i in range(2,a):
        if a%i==0:
            flag=False
            break
    return flag

#5
def bank(a:float,years:int)->float:
    """
    """
    for i in range(a):
        years=years+years*0.1
    return years


#4
def season(n:int)->str:
    """
    """
    if n==12 or 1<= n <=2:
        n=("Talv")
    elif 3<= n <=5:
        n=("Kevad")
    elif 6<= n <=8:
        n=("Suvi")
    elif 9<= n <=11:
        n=("Sügis")
    return n


#3
def square(a:float)->float:
   """pindala läbimõõt diagonale leidmine
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



