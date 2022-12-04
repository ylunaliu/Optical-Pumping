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
import string
frequency = np.array([0, 0.05, 0.09, 0.13, 0.17])
voltage_1 = np.array([0.304, 0.424, 0.523, 0.608, 0.696])
voltage_2 = np.array([0.304, 0.485, 0.616, 0.75, 0.901])
voltage_err = 0.0136*np.ones(len(voltage_2))/np.sqrt(10)



def f1(x, m, b):
    return m*(x)+b


Magnetic_field_given_energy_87  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/2)*10000
popt3, pcov3 = scipy.optimize.curve_fit(f1, voltage_1, Magnetic_field_given_energy_87 ) 
y_fit3 = f1(voltage_1, *popt3)
print(popt3)

emodel3 = lm.Model(f1)
params3 = emodel3.make_params(m = 0.6, b=0)
ymodel3 = emodel3.eval(params3, x=Magnetic_field_given_energy_87)
result3=emodel3.fit(voltage_1, params3, x= Magnetic_field_given_energy_87, weights = 1/voltage_err,scale_covar=False)
print(result3.fit_report())

Magnetic_field_given_energy_85  = 4.136*10**(-15)*frequency*10**6/((5.8*10**(-5))*1/3)*10000





emodel = lm.Model(f1)
params = emodel.make_params(m = 0.6, b=0)
ymodel = emodel.eval(params, x=frequency)
# result=emodel.fit(voltage_1, params, x= frequency, weights= voltage_err)
result=emodel.fit(voltage_1, params, x= frequency, weights= 1/voltage_err,scale_covar=False)
print(f"Here is the report for 87 {result.fit_report()}")
m = result.params['m'].value
b = result.params['b'].value
m_err =  result.params['m'].stderr
b_err = result.params['b'].stderr

emodel2 = lm.Model(f1)
params2 = emodel.make_params(m = 0.6, b=0)
ymodel2 = emodel.eval(params2, x=frequency)
result2=emodel.fit(voltage_2, params2, x= frequency, weights=1/voltage_err,scale_covar=False)
print(f"Here is the report for 85 {result2.fit_report()}")
m1= result2.params['m'].value
b1 = result2.params['b'].value
m1_err =  result2.params['m'].stderr
b1_err = result2.params['b'].stderr



fig, axs = plt.subplots(2,figsize=(8,10))

axs[0].plot(frequency, result2.best_fit, label = r"${}^{85} Rb$", linestyle="-")
axs[0].plot(frequency, result.best_fit, label = r"${}^{87} Rb$", linestyle="-.")
axs[0].legend(fontsize = 17)
axs[0].errorbar(frequency,voltage_1,  yerr = voltage_err,  fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")
axs[0].errorbar( frequency, voltage_2, yerr = voltage_err,  fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")

axs[0].grid(color='0.95', linestyle='-', linewidth=1)
axs[0].set_ylabel("Sweep coil current (A)", fontsize = 22)
axs[0].set_xlabel("Transition Frequency (MHz)", fontsize = 22)
axs[0].xaxis.set_tick_params(labelsize=18)
axs[0].yaxis.set_tick_params(labelsize=18)

axs[1].plot(Magnetic_field_given_energy_87,result3.best_fit, 'r-')
axs[1].errorbar(Magnetic_field_given_energy_87,voltage_1, yerr = voltage_err, fmt = "r.",  elinewidth=1, markersize=3, capsize=3, color="k")
axs[1].grid(color='0.95', linestyle='-', linewidth=1)

axs[1].set_ylabel("Sweep coil current (A)", fontsize = 22)
axs[1].set_xlabel("Magnetic field (Gauss)",fontsize = 22)
axs[1].xaxis.set_tick_params(labelsize=18)
axs[1].yaxis.set_tick_params(labelsize=18)
for n, ax in enumerate(axs):
    ax.text(-0.1, 1.1, string.ascii_uppercase[n], transform=ax.transAxes, 
            size=20, weight='bold')
fig.tight_layout()

plt.savefig('twoisoptoes.pdf',bbox_inches='tight')  



# plt.plot(frequency, voltage_1, 'k.')
# plt.plot(frequency, voltage_2, 'k.')
# plt.plot(frequency, result2.best_fit, label = r"${}^{85} Rb$")
# plt.plot(frequency, result.best_fit, label = r"${}^{87} Rb$")
# plt.xlabel("Transition Frequency (MHz)", fontsize = 16)
# plt.ylabel("Sweep coil current (A)", fontsize = 16)
# plt.legend()
plt.show()



m_85 = uc.ufloat(m, m_err)
m_87 = uc.ufloat(m1, m1_err)
print(m, m1)
ratio = m_87/m_85
print(ratio)