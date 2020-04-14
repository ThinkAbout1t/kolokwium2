'''Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
dobutok=1
for i in range(10):
    a[i]=random.randint(-5,10)
    if a[i]!=0:
        dobutok*=a[i]
print(a)
print(dobutok)
