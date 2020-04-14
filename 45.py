'''Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
виконал Пахомов Олександр'''
import math
l=[]
r=int(input('radiys:'))
for i in range(1,5):
    h=math.sqrt(r**2-((i*r)/5)**2)
    l.append(h)
    l.append(h)
l.append(r)
print(sorted(l))
