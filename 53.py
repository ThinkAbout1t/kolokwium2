'''В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
виконал Пахомов Олександр'''
import numpy as np
import random
l=[0,1,5]
n=int(input('size:'))
a=np.zeros(n, dtype= int)
for i in range(n):
    a[i]=random.choice(l)
print(sorted(a))
