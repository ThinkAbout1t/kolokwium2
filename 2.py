'''Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
виконав Пахомов Олександр 122-А'''
import numpy as np
import math
a=np.zeros(5,dtype=int)
for i in range(5):
    a[i]= int(input(''))
print(a)
b=a.copy()
for i in range(5):
    a[i]=math.sqrt(a[i])
print(a)
for i in range(5):
    b[i]=b[i]*b[i]
print(b)
