'''Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
виконал Пахомов Олександр'''
import numpy as np
import random
l=[]
a=np.zeros(10, dtype= int)
c=0
k=0
for i in range(10):
    a[i]=random.randint(1,20)
for i in range(10):   
    if i%2==0:
        l.append(a[i])
print(a)
print(l)
m=max(l)
print(m)
print(l.count(m))
for i in range(len(l)):
    if l[i]==m:
        k+=1
if k==1:
    print('one max element')
else:
    print('more than one max element')
