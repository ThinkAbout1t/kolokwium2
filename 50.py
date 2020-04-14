'''У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(100, dtype= int)
n=int(input('nomer:'))
for i in range(100):
    a[i]=random.randint(10000000,100000000)
x=np.random.choice(a,10)
print(x)
if n in x:
    print('VICTORY!!!!!')
else:
    print('LOSE(((')
