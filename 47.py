'''У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(10, dtype= int)
for i in range(10):
    a[i]=int(input('number:'))
m=a.max()
index=list(a).index(a.max())
new_a=np.insert(a,index+1,index)
print(new_a)
