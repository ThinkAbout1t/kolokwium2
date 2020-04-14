'''Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
виконал Пахомов Олександр'''
import numpy as np
l=[]
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=int(input('number:'))
    if -2<a[i]<10:
        l.append(a[i])
seredny=sum(l)//len(l)
print(seredny)
