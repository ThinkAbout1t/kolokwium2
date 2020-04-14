'''Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
виконав Пахомов Олександр 122-А'''
import numpy as np
import random
a=np.zeros(15, dtype= int)
for i in range(15):
    a[i]= random.randint(-15,30)
print(a)
print(a.max())
print(list(a).index(a.max()))
