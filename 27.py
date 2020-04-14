'''Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
виконал Пахомов Олександр'''
import numpy as np
import random
a=np.zeros(12, dtype=int)
summa=0
c=0
for i in range(12):
    a[i]=random.randint(10,50)
    summa+=a[i]
    if a[i]<30:
        c+=1
print(a)
print(f'summa:{summa}')
print(f'serednya:{a.mean()}')
print(f'k posushlivix:{c}')
print(f'nayposushlivi:{a.min()}')
