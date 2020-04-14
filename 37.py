'''Розсортуйте заданий лінійний масив по зростанню.
Виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(10, dtype=int)
for i in range(10):
    a[i]=int(input('number:'))
print(a)
print(sorted(a))
