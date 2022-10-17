import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

freq = 12
rate = 0.05
rate_2 = 0.12
years = 5
pv = 120000
saved_money = 100000

nper = years * freq  # liczba wszystkich okresów


def house_worth():
    np.set_printoptions(suppress=True)

    principal_increasing = np.around(np.zeros(years)+ (pv*rate))
    principal_increasing[:5]

    balance = np.zeros(years) + pv
    balance_close = np.around(balance + np.cumsum(principal_increasing),2)
    sums= balance_close[[0,1,2,3,4]]
    return balance_close[[4]] , sums
    # wartość mieszkania 150000 zł
    
def installement_worth(sums):
    np.set_printoptions(suppress=True)

    principal_decreasing = np.around(np.zeros(nper)+(sums[4]/nper),2)

    return principal_decreasing[:1]
    # należy wpłacać po 2500 zł

def chart_data():
    rate_v = rate/freq
    balance = np.zeros(nper) + pv
    increasing= np.around(np.zeros(nper)+ (pv*rate_v))
    balance_close_1 = np.around(balance + np.cumsum(increasing),2)
    # wartość mieszkania miesięczna
    rate_y= rate_2/freq
    balance = np.zeros(nper) + saved_money
    increasing_2 = np.around(np.zeros(nper)+ (pv*rate_y))
    balance_close_2 = np.around(balance + np.cumsum(increasing_2),2)
    #ilość uzbieranych pieniędzy
    return balance_close_1 , balance_close_2 



def chart(balance_close_1 , balance_close_2):
    plt.plot(balance_close_1,label='wartość mieszkania')
    plt.plot(balance_close_2,label='ilość pieniędzy')
    plt.legend()
    plt.xlabel('Liczba okresów')
    plt.ylabel('Skumulowana wartość')
    plt.show()

balance_close , sums = house_worth()
principal_decreasing = installement_worth(sums)
print(f'Wartość mieszkania po 5 latach {balance_close}')
print(f'Pojedyńcza ilość pieniędzy która należy odłożyć co miesiąc {principal_decreasing}')
balance_close_1 , balance_close_2 = chart_data()
chart(balance_close_1 , balance_close_2)
