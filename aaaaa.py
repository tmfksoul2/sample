import os
import pandas
a = 8
b = 2

scores = [1, 3, 4, a, b]

for score in scores:
    if score == 0:
        print('失格です')
    elif score < 5:
        print('追試です')
    else:
        print('合格です')