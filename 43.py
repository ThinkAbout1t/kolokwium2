'''Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
виконал Пахомов Олександр'''
import numpy as np
w=False
a=np.zeros(10, dtype= int)
x=int(input('zadane:'))
b=int(input('zadane:'))
c=0
for i in range(10):
    a[i]=int(input('number:'))
for i in range(10):
    if a[i]%x==0 and a[i]%b!=0:
        w=True
print(w)
