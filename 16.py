'''Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
import random
a=np.zeros(15, dtype= int)
dobutok=1
for i in range(15):
    a[i]=random.randint(10,50)
    if a[i]%7==0:
        dobutok*=a[i]
print(a)
print(dobutok)
