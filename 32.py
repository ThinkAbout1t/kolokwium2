'''Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
виконал Пахомов Олександр'''
import numpy as np
t=False
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=int(input('number:'))
    if a[i]<0 and a[i]%2==0:
        t=True
print(t)
