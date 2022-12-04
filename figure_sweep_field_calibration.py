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
voltage_2 = np.array([0.304, 0.49, 0.616, 0.75, 0.901])
voltage_err = 0.0136*np.ones(len(voltage_2))

def f1(x, m, b):
    return m*(x)+b

Magnetic_field_given_energy_87  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/2)*10000
popt3, pcov3 = scipy.optimize.curve_fit(f1, voltage_1, Magnetic_field_given_energy_87 ) 
y_fit3 = f1(voltage_1, *popt3)
print(popt3)

emodel = lm.Model(f1)
params = emodel.make_params(m = 0.6, b=0)
ymodel = emodel.eval(params, x=voltage_1)
result=emodel.fit(Magnetic_field_given_energy_87, params, x= voltage_1, sigma = voltage_err)
print(result.fit_report())

Magnetic_field_given_energy_85  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/3)*10000

emodel2 = lm.Model(f1)
params2 = emodel.make_params(m = 0.6, b=0)
ymodel2 = emodel.eval(params, x=Magnetic_field_given_energy_85)
result2=emodel.fit(voltage_2, params, x= Magnetic_field_given_energy_85, sigma = voltage_err)
print(result2.fit_report())


plt.plot(Magnetic_field_given_energy_87,result.best_fit, '-')
plt.plot(Magnetic_field_given_energy_85,result2.best_fit, '-')
plt.errorbar(Magnetic_field_given_energy_87,voltage_1, yerr = voltage_err, fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")
grid(color='0.95', linestyle='-', linewidth=1)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel("Sweep coil current (A)", fontsize = 16)
plt.xlabel("Magnetic field (Gauss)",fontsize = 16)



plt.show()