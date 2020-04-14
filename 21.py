'''Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype=int)
dobutok=1
k=int(input('number:'))
for i in range(10):
    a[i]=random.randint(50,100)
    if a[i]<k:
        dobutok*=a[i]
print(a)
print(dobutok)
