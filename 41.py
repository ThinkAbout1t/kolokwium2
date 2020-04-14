'''Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
виконал Пахомов Олександр'''
import numpy as np
t=False
a=np.zeros(10, dtype= int)
x=int(input('zadane:'))
c=0
for i in range(10):
    a[i]=int(input('number:'))
m=a.max()
print(m)
for i in range(10):
    if a[i]==m:
        c+=1
        print(c)
if c==1:
    if m<x:
        t=True
print(t)
