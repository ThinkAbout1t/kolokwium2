'''Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
виконав Пахомов Олександр 122-А
'''
import numpy as np
a=np.zeros(5, dtype= int)
for i in range(5):
    a[i]= int(input(''))
print(list(a))
print(a.mean())
