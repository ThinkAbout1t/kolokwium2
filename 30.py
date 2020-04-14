'''Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
виконал Пахомов Олександр'''
import numpy as np
l=[]
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=int(input('number:'))
ind=list(a).index(a.min())
for i in range(ind+1,10):
        l.append(a[i])
seredny=sum(l)//len(l)
print(seredny)
