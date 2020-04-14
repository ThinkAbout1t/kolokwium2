'''Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(20, dtype= int)
summa=0
for i in range(20):
    a[i]=random.randint(150,300)
s=a.mean()
print(a)
print(s)
for i in range(10):
    if a[i]<s:
        summa+=a[i]
print(summa)
