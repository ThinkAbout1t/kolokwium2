'''Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=random.randint(1,5)
bc = np.bincount(a)
print(a)
print(bc)
print(bc.argmax())
