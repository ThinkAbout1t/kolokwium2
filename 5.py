'''Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
виконав Пахомов Олександр 122-А'''
import numpy as np
import random
a=np.zeros(7, dtype= int)
for i in range(7):
    a[i]= random.randint(0,20)
print(a)
for i in range(7):
    a[i]*= 2
print(a)
