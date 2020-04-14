'''Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
виконал Пахомов Олександр'''
import numpy as np
l=[]
a=np.array(['qqq','wwe','qtq','www','qqw','ewq','poi','hgd'])
b=np.array([1233,3312,3123,4444,1111,3145,2222,5111])
avar=b.mean()
for i in range(8):
    c=b[i]-avar
    l.append(abs(c))
m=l.index(min(l))
print(avar)
print(a[m])
i1=list(b).index(b.max())
print(a[i1])
b_new=np.delete(b,i1)
a_new=np.delete(a,i1)
i2=list(b_new).index(b_new.max())
print(a[i2])
i3=list(b).index(b.min())
a_new1=np.delete(a,i3)
b_new1=np.delete(b,i3)
print(a_new1)
print(b_new1)
