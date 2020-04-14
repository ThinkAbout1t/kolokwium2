'''Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
виконал Пахомов Олександ'''
import numpy as np
import random
l=[]
c=0
a=np.zeros(20, dtype= int)
for i in range(20):
    a[i]=random.randint(1,5)
for i in range(19):
    if a[i]==a[i+1]:
        c+=1
        l.append(c)
    else:
        c=0
        print(l)
print(a)
print(max(l)+1)
