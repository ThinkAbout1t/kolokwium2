'''У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(30, dtype= int)
b=np.arange(1,31)
c=0
for i in range(30):
    a[i]=random.randint(1,7)
    if a[i]>5:
        c+=1
print(a)
for i in range(15):
    b[i],b[-(i+1)]=b[-(i+1)],b[i]
print(b)
print(c)
