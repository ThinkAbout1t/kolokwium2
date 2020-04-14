'''Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
import random
a=np.zeros(20, dtype= int)
summa=0
for i in range(20):
    a[i]=random.randint(100,200)
    if i%2!=0:
        summa+=a[i]

'''
for i in range (1,21,2):
    summa+=a[i]
'''
print(a)
print(summa)
