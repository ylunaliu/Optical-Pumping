import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize
from scipy.signal import medfilt
from pylab import *
from scipy.signal import savgol_filter  
import lmfit as lm

# Find the error flatuation
def f1(x, m, b):
    return m*(x)+b

voltage = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0019.CSV",delimiter=",", usecols=(3,4))
xv_time = voltage[500:len(voltage)-500,0]
voltage = voltage[500:len(voltage)-500,1]

emodel=lm.Model(f1)
params = emodel.make_params(m=2, b=1)
ymodel = emodel.eval(params,  x= xv_time)


result=emodel.fit(voltage, params, x= xv_time)
# print(result.fit_report())
# print(result.params['b'].value)
# print(result.params['b'].stderr)


m = result.params['m'].value
b = result.params['b'].value
m_err =  result.params['m'].stderr
b_err = result.params['b'].stderr

y_fit = f1(xv_time, m ,b)


position_time = np.array([1.1272, 1.126, 1.126, 1.124, 1.124, 1.1248,1.1252, 1.1264,1.1256,1.1248])
y_fit2 = f1(position_time, m, b)
stdev = np.std(position_time)
# standerr = stdev/np.sqrt(len(position_time))

print(stdev)




plt.plot(position_time, y_fit2, '.')
# plt.plot(xv_time, voltage)
plt.show()

stdev1 = np.std(y_fit2)
standerr1 = stdev1/np.sqrt(len(y_fit2))

print(stdev1)
print(standerr1)







# def gauss(x, H, A, x0, sigma):
#     return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


# def f1(x, m, b):
#     return m*(x)+b

# signal = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/CH1NOV7.CSV",delimiter=",")

# start = 1140#680
# stop = len(signal) -1150
# x_time = signal[start:stop,0]
# dip = signal[start:stop,1]
# # dip = medfilt(dip,1)
# Voltage = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/CH2NOV7.CSV",delimiter=",")
# xv_time = Voltage[start:stop,0]
# voltage = medfilt(Voltage[start:stop,1],7)



# #I would need to smooth the data


# popt, pcov = scipy.optimize.curve_fit(gauss,xv_time, voltage, maxfev=5000) 
# print(*popt)
# y_fit2 = gauss(xv_time, *popt)


# popt, pcov = scipy.optimize.curve_fit(gauss,y_fit2, dip, p0=[0, -2.1,0.3,0.005],maxfev=5000) 
# print(*popt)
# dip_final = gauss(y_fit2, *popt)

# # plt.plot(xv_time, y_fit2)
# # plt.plot(x_time,dip, 'b.')
# plt.plot(y_fit2, dip_final, 'k-')
# plt.plot(y_fit2, dip, '.')
# # p0=[0, -2.1,0.3,0.005]
# # plt.plot(y_fit2, gauss(y_fit2, *p0))
# # plt.plot(x_time, dip)
# # plt.plot(xv_time, voltage, 'r.')
# plt.show()