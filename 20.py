'''Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
import random
a=np.zeros(20, dtype= float)
summa=0
k=int(input('number:'))
for i in range(20):
    a[i]=random.randint(50,100)
    if a[i]>k:
        summa+=a[i]
print(a)
print(summa)
