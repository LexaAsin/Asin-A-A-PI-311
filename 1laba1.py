# -*- coding: utf-8 -*-
"""1laba1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BcQbjf4fIPXBqCy7AOb-isv_5RoN4xvu
"""

a=int(input("знач:"))
b=int(input("знач:"))
c=int(input("знач:"))
P=int(a)+int(b)+int(c)
p=P/2
pd=(p*(p-a)*(p-b)*(p-c))**0.5
print(P,p,pd)
#найти периметр и площадь треугольника

a=int(input("Знач:"))
b=int(input("Знач:"))
#(a+b)**2=a**2+2*a*b+b**2
print(a**2+2*a*b+b**2,(a+b)**2)

a=int(input("Знач:"))
b=int(input("Знач:"))
print((a+b)**2)

a=5
b=int(input("знач:"))
print(a*b)

a=15
b=10
c=int(input("знач:"))
print((a+b)/c)

a=int(input("знач:"))
b=int(input("знач:"))
print(((a**3+14)/5)*b)#убивает неравенство

a=float(input(""))
b=float(input(""))
if a%b==0:
  print(a/b)#деление двух дробных чисел без остатка

a=int(input('знач:'))
n=int(input('знач:'))
print(a**2//n)

a=int(input("знач:"))
b=int(input("знач:"))
print(a*b)#умножение 2 натуральных чисел

a=int(input("знач:"))
b=int(input("знач:"))
print(a%b)#получение остатка без деления

n=int(input("знач:"))
print(n//(60*60*24),':',n//(60*60),':',n//60)#повышенная сложность 1

n=int(input("знач:"))
t=str(n)
t2=t+t
t3=t+t+t
comp=n+int(t2)+int(t3)
print("ответ:",comp)#повышенная сложность 2