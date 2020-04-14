'''Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
Виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype=int)
b=np.zeros(10, dtype=int)
c=0
print('північний-1; південний-2; східний-3; західний-4')
for i in range(10):
    a[i]=int(input('direction:'))
for i in range(10):
    b[i]=int(input('power:'))
for i in range(10):
    if a[i]==2:
        if b[i]>8:
            c+=1
print(c)
