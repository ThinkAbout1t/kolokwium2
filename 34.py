'''Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
b=np.zeros(10, dtype= int)
c=np.zeros(10, dtype= int)
dobutok=1
for i in range(10):
    a[i]=random.randint(-5,10)
for i in range(10):
    b[i]=random.randint(-5,10)
for i in range(10):
    c[i]=a[i]*b[i]
print(a)
print(b)
print(c)
