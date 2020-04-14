'''Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
виконал Пахомов Олександр'''
import numpy as np
a=np.zeros(20, dtype= int)
for i in range(20):
    a[i]=int(input('number:'))
new_a=set(a)
print(a)
print(new_a)
if len(a)==len(new_a):
    print('no same elements')
else:
    print('same elements')
