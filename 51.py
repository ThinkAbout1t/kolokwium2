'''Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
виконал Пахомов Олександр'''
import numpy as np
import random
l=[]
a=np.zeros(10, dtype= int)
c=0
for i in range(10):
    a[i]=random.randint(1,20)
    index=list(a).index(a[i])
    if a[i]>index+10:
        c+=1
        l.append(a[i])
print(a)
if c==0:
    print('no elements')
else:
    print(l)
