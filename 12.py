'''Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
a=np.zeros(10, dtype= int)
c=0
for i in range(10):
    a[i]= int(input('temperatura:'))
s=a.mean()
print(s)
for i in range(10):
    if a[i]>s:
        c+=1
print(c)
