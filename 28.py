'''Знайти кількість парних елементів одновимірного масиву.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(20, dtype= int)
summa=0
for i in range(20):
    a[i]=random.randint(100,200)
    if a[i]%2==0:
        summa+=1
print(a)
print(summa)
