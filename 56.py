'''Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
виконал Пахомов Олександр'''
import numpy as np
import random
t=False
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=random.randint(1,5)
for i in range(8):
    if a[i]==a[i+1]==a[i+2]:
        t=True
print(a)
print(t)
