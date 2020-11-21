from random import randint
from matplotlib import pyplot as plt
import seaborn as sb
import math
for x in range(1, 50):
    if 0 != 100 * x / 100 - x:
        print(x)

# zadanie 2
fig, axes = plt.subplots(4, 2, figsize=(18,10))

x_var = [10, 2, -2, -10]
plots = ([0,0],[1,0],[2,0],[3,0])
y = []
sum = 0
N = 50
for plot, x in zip(plots, x_var):
    print()
    y = []
    sum = 0
    for i in range(N):
        sum += pow(x, i) / math.factorial(i)
        y.append(sum)
    print(round(y[-1],6), 'in compere to e^x:',round(math.exp(x),6))
    error_value = [(math.exp(x)-value)/math.exp(x) for value in y]
    axes[plot[0], plot[1]].set_title('suma czesciowa dla x={}'.format(x))
    sb.lineplot(ax=axes[plot[0], plot[1]], x=range(N), y=y, color="#9ad92e")
    sb.lineplot(ax=axes[plot[0], plot[1]+1], x=range(N), y=error_value)
    plt.setp(axes[plot[0], plot[1]], xlabel='x axis label')
    plt.setp(axes[plot[0], plot[1]], ylabel='suma czesciowa')
    plt.setp(axes[plot[0], plot[1]+1], xlabel='x axis label')
    plt.setp(axes[plot[0], plot[1]+1], ylabel='blad wzgledny')
plt.subplots_adjust(hspace=0.5)
plt.show()


# [pow(x[-1], i) / math.factorial(i) for i in range(50)]
#
#
#
#
# # zadanie 3
# x, y = pow(9.8,201), pow(10.2,199)
# math.sqrt(pow(x,2) + pow(y,2))
# y * math.sqrt(pow(x/y,2) +1)

# a, c = 1, 1
# b_possible = [randint(int(pow(10,7.4)+1), int(pow(10,8.5))) for i in range(10)]
# math.copysign(1, b_possible[0])
#
