'''Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
a=np.zeros(10, dtype= int)
dobutok=1
for i in range(10):
    a[i]= int(input('number:'))
    if a[i]<0:
        dobutok*=a[i]
print(a)
print(dobutok)
