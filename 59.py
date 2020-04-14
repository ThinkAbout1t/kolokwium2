'''Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
виконал Пахомов Олександ'''
import numpy as np
import random
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=random.randint(1,10)
new_a=set(a)
print(a)
print(len(new_a))
