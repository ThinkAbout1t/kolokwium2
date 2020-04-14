'''Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
виконал Пахомов Олександр'''
import numpy as np
import math
a=np.zeros(10, dtype= int)
c=0
for i in range(10):
    a[i]=int(input('number:'))
    if i*i<a[i]<math.factorial(i):
        c+=1
print(c)
