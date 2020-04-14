'''Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
виконал Пахомов Олександр'''
import numpy as np
a=np.array(['qqq','wwe','qtq','www','qqw','ewq','poi','hgd'])
b=np.array([12,31,23,13,55,44,76,98])
g=int(input('cost:'))
for i in range(8):
    if b[i]==g:
        index=list(a).index(a[i])
new_a=np.delete(a,np.s_[:index])
new_b=np.delete(b,np.s_[:index])
print(new_a)
print(new_b)
