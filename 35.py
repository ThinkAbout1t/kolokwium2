'''Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Виконал Пахомов Олекcандр'''
import numpy as np
a=np.zeros(10, dtype=int)
c=0
for i in range(10):
    a[i]=int(input('number:'))
for i in range(9,0,-1):   
    if a[i]<a[i-1]:
        pass
    else:
        c+=1
if c!=0:
    print('no')
else:
    print('yes')
    
