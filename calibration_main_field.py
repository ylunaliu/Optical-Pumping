import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from time import time
from tkinter import font
from pylab import *
import uncertainties as uc
import scipy.odr as od
import lmfit as lm

frequency = np.array([0, 0.2, 0.4, 0.6, 0.8])
Total_Magnetic_field_87 = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/2)*10000
# Total_Magnetic_field_85 = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/3)*10000
voltage_err = 0.0015*np.ones(len(frequency))

def f1(x, m, b):
    return m*(x)+b


Amps = 2*np.array([0, 0.0183, 0.0384, 0.05615, 0.076])
voltage_1_sweep = np.array([0.304,0.3, 0.16, 0.128, 0.024])
# voltage_2_sweep = np.array([0.304,0.64, 0.624, 0.832, 0.968])
magnetic_field_sweep_1 = 0.618*voltage_1_sweep-0.19
# magnetic_field_sweep_2 = 0.618*voltage_2_sweep-0.19 

main_field_87 = Total_Magnetic_field_87 - magnetic_field_sweep_1 
emodel = lm.Model(f1)
params = emodel.make_params(m = 0.1, b=0.001)
ymodel = emodel.eval(params, x=main_field_87)
result=emodel.fit(Amps, params, x= main_field_87, weights = 1/voltage_err)
print(result.fit_report())
# popt, pcov = scipy.optimize.curve_fit(f1, Amps, main_field_87) 
# y_fit2 = f1(Amps, *popt)

emodel_reverse =  lm.Model(f1)
# params_r = emodel.make_params(m = 0.6, b=1)
# ymodel_r = emodel.eval(params, x=Amps)
# result_r=emodel.fit(main_field_87, params, x= Amps, weights = 1/voltage_err)
# print(result_r.fit_report())

plt.plot(main_field_87, result.best_fit, 'r-')
grid(color='0.95', linestyle='-', linewidth=1)
plt.errorbar(main_field_87,Amps, yerr = voltage_err, fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")
grid(color='0.95', linestyle='-', linewidth=1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel("Main coil current (A)", fontsize = 22)
plt.xlabel("Magnetic field (Gauss)",  fontsize = 22)
plt.show()

# plt.plot(Amps, main_field_87, '.')
# plt.plot(Amps, result_r.best_fit, label = "y = {:.2f}x+{:.2f}".format(result_r.params['m'].value, result_r.params['b'].value))
# plt.xlabel("Main coil current (A)", fontsize = 12)
# plt.legend()
# plt.ylabel("Magnetic field (Gauss)",  fontsize = 12)
# plt.title("Main field calibration")
# plt.show()

# Next do the linear zeeman effect
# emodel2 = lm.Model(f1)
# params2 = emodel.make_params(m = 0.6, b=0)
# ymodel2 = emodel.eval(params, x=frequency)
# result2=emodel.fit(Amps, params, x= frequency, weights = voltage_err)
# print(result2.fit_report())
# plt.plot(frequency, result2.best_fit)
# plt.errorbar(frequency, Amps, yerr = voltage_err, fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")
# grid(color='0.95', linestyle='-', linewidth=1)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.xlabel("Frequency (MHz)", fontsize = 16)
# plt.ylabel("Magnetic field (Gauss)",  fontsize = 16)
# plt.show()
# plt.show()
