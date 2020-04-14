'''Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Bиконал Пахомов Олександр 122-А'''
import numpy as np
a=np.zeros(15, dtype= int)
for i in range(15):
    a[i]= int(input('number:'))
print(a.min())
