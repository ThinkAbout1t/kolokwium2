'''Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
a=np.zeros(10, dtype= int)
c=0
for i in range(10):
    a[i]= int(input('temperatura:'))
    if a[i]>15:
        c+=1
print(c)
