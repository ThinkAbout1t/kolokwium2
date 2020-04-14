'''Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
виконав Пахомов Олександр 122-А'''
import numpy as np
x = np.array (['qweqwe', 'dasdas', 'sdggdfgdg', 'qqq', 'www'])
print(x)
b=input('symbol: ')
for i in range(len(x)):
    for j in range(len(x[i])):
        if j == 0:
            if x[i][j]==b:
                print(x[i])
        
