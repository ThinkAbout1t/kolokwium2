'''Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
dobutok=1
for i in range(10):
    a[i]=random.randint(5,500)
    if a[i]%3==0 and a[i]%9==0:
        dobutok*=a[i]
print(a)
print(dobutok)
