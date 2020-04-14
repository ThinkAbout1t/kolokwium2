'''Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(10, dtype= int)
summa=0
x=int(input('input:'))
for i in range(10):
    a[i]=int(input('number:'))
for i in range(10):
    if a[i]==x:
        break
    else:
        if a[i]%2==0:
            summa+=1
print(summa)
