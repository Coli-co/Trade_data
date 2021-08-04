import pandas as pd
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt


def times_and_cumulativeprofitandloss():
    temp = []
    temp1 = []
    for i in range(len(df["Times"])):
        times = df["Times"][i]
        temp.append(times)
    # print(temp)
    for j in range(len(df["Cumulative_ profit_and_loss"])):
        result = df["Cumulative_ profit_and_loss"][j]
        temp1.append(result)
    # print(temp1)
    return temp, temp1


"""
Used for plotting where x-axis = times,
 y-axis = cumulative_profit_and_loss
if q = times_and_cumulativeprofitandloss()
data of times : q[0]
data of cumulative_profit_and_loss : q[1]
"""


font1 = {'family': 'serif', 'color': 'blue', 'size': 18}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 12}

# A1 Short Strategy
df = pd.read_csv(
    'D://timothyTest/readfile_plot/Long_strategies_net_momentum_A1.csv')
a = times_and_cumulativeprofitandloss()
x = np.array(a[0])
y = np.array(a[1])
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("A1 Short Strategy", loc='left', fontdict=font1)
plt.xlabel("Trade Times", fontdict=font2)
plt.ylabel("Stategy Net Momentum", fontdict=font2)

# A2 Short Strategy
df = pd.read_csv(
    'D://timothyTest/readfile_plot/Long_strategies_net_momentum_A2.csv')
b = times_and_cumulativeprofitandloss()
x = np.array(b[0])
y = np.array(b[1])
plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("A2 Short Strategy", loc='left', fontdict=font1)
plt.xlabel("Trade Times", fontdict=font2)
plt.ylabel("Strategy Net Momentum", fontdict=font2)

# A3 Short Strategy
df = pd.read_csv(
    'D://timothyTest/readfile_plot/Long_strategies_net_momentum_A3.csv')
c = times_and_cumulativeprofitandloss()
x = np.array(c[0])
y = np.array(c[1])
plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("A3 Short Strategy", loc='left', fontdict=font1)
plt.xlabel("Trade Times", fontdict=font2)
plt.ylabel("Strategy Net Momentum", fontdict=font2)

# Trading times of A4 are too few times
# A4 Short Strategy
# df = pd.read_csv(
#     'D://timothyTest/readfile_plot/Long_strategies_net_momentum_A4.csv')
# d = times_and_cumulativeprofitandloss()
# x = np.array(d[0])
# y = np.array(d[1])
# plt.subplot(2, 3, 4)
# plt.plot(x, y)
# plt.title("A4 Short Strategy", loc='left', fontdict=font1)
# plt.xlabel("Trade Times", fontdict=font2)
# plt.ylabel("Strategy Net Momentum", fontdict=font2)

# A7 Short Strategy
# df = pd.read_csv(
#     'D://timothyTest/readfile_plot/Long_strategies_net_momentum_A7.csv')
# e = times_and_cumulativeprofitandloss()
# x = np.array(e[0])
# y = np.array(e[1])
# plt.subplot(2, 3, 5)
# plt.plot(x, y)
# plt.title("A7 Short Strategy", loc='left', fontdict=font1)
# plt.xlabel("Trade Times", fontdict=font2)
# plt.ylabel("Strategy Net Momentum", fontdict=font2)


plt.show()
