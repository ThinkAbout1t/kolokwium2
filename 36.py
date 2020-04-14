'''Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(10, dtype=int)
summa=0
for i in range(10):
    a[i]=int(input('number:'))
    if a[i]>0:
        summa+=a[i]
print(a)
print(summa)
