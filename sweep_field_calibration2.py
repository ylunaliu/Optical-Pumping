import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from time import time
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from pylab import *
import uncertainties as uc
import scipy.odr as od
import lmfit as lm
frequency = np.array([0, 0.05, 0.09, 0.13, 0.17])
voltage_1 = np.array([0.304, 0.424, 0.52, 0.608, 0.696])
voltage_2 = np.array([0.304, 0.48, 0.616, 0.76, 0.904])

def f1(x, m, b):
    return m*(x)+b

# The magnetic field 
popt, pcov = scipy.optimize.curve_fit(f1, voltage_1, frequency) 
y_fit2 = f1(voltage_1, *popt)
popt2, pcov2 = scipy.optimize.curve_fit(f1, voltage_2, frequency) 
y_fit22 = f1(voltage_2, *popt2)


Magnetic_field_given_energy_87  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/2)*10000
popt3, pcov3 = scipy.optimize.curve_fit(f1, voltage_1, Magnetic_field_given_energy_87 ) 
y_fit3 = f1(voltage_1, *popt3)
print(popt3)

emodel = lm.Model(f1)
params = emodel.make_params(m = 0.6, b=0)
ymodel = emodel.eval(params, x=voltage_1)
result=emodel.fit(Magnetic_field_given_energy_87, params, x= voltage_1)
print(result.fit_report())

Magnetic_field_given_energy_85  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/3)*10000
# plt.plot(voltage_2, frequency, '.')
# plt.plot(voltage_2, y_fit22, label = "85Rb y = {:.3f}x + {:.2f}".format(popt[0], popt[1]))
# plt.plot(voltage_1, frequency, '.')
# plt.plot(voltage_1, y_fit2, label = "87Rb y = {:.3f}x + {:.2f}".format(popt2[0], popt2[1]))
# plt.plot(voltage_1, Magnetic_field_given_energy_87, '.', label = "y = {:.3f}x + {:.3f}".format(popt3[0], popt3[1]))
plt.plot(voltage_1, y_fit3, '-')
plt.errorbar(voltage_1, Magnetic_field_given_energy_87, xerr = np.ones(len(voltage_1))*0.02, fmt = "r.",  elinewidth=1, markersize=5, capsize=3, color="k")
# plt.plot(voltage_2, Magnetic_field_given_energy_85, '.')
grid(color='0.95', linestyle='-', linewidth=1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend()
plt.xlabel("Sweep coil current (A)")
plt.ylabel("Magnetic field (Gauss)")
plt.title("Sweep Field Calibration")
print(*popt)
print(*popt2)
plt.show()