'''Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Виконал Пахомов Олександр'''
import numpy as np
l=[]
a=np.zeros(10, dtype= int)
summa=0
for i in range(10):
    a[i]=int(input('number:'))
for i in range(10):
    if a[i]==0:
        break
    else:
        l.append(a[i])
for i in range(len(l)):
    if l[i]%2==0:
        summa+=l[i]
print(a)
print(l)
print(summa)
