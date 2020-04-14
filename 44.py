'''Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(10, dtype= int)
c=0
for i in range(10):
    a[i]=int(input('number:'))
    if a[i]==i and a[i]%3==0:
        c+=1
print(c)
