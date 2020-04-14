'''Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(30, dtype= int)
summa=0
for i in range(30):
    a[i]=random.randint(500,1000)
    if a[i]%5==0 and a[i]%8==0:
        summa+=a[i]
print(a)
print(summa)
