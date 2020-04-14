'''Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
dobutok=1
for i in range(10):
    a[i]=random.randint(10,100)
    if a[i]%5==0:
        dobutok*=a[i]
print(a)
print(dobutok)
