import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import lmfit as lm
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from pylab import *
import uncertainties as uc
import scipy.odr as od
# Position of the peaks for 87Rb for the last four large peak: [-0.0491 -0.0278  0.0021  0.0346], voltage = [ 9.   9.6 10.4 11.2]

main_field = 8.71*0.512*2

def f1(x, m, b):
    return m*(x)+b
# test = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/Current_Nov7.CSV",delimiter=",")
# print(test[:,1])
# plt.plot(test[:,0],test[:,1],'.')
# plt.show()
voltage2 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/1Rb87CH1.CSV",delimiter=",")[:,1]
voltage1 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/NOV16-CH2.CSV",delimiter=",")
time =voltage1[:,0]
voltage = voltage1[:,1]
print(voltage)

emodel3 = lm.Model(f1)
params3 = emodel3.make_params(m = 0.6, b=0)
ymodel3 = emodel3.eval(params3, x=time)
result3=emodel3.fit(voltage, params3, x= time,scale_covar=False)
print(result3.fit_report())
m = result3.params['m'].value
b = result3.params['b'].value
m_err =  result3.params['m'].stderr
b_err = result3.params['b'].stderr
print(m,b)
fit_voltage = time*m+b
# plt.plot(time, fit_voltage)
# plt.plot(time, voltage)
# plt.show()

print(fit_voltage - 6.4)
sweep_field = 0.618*fit_voltage-0.19
print(voltage)
total_field = sweep_field+main_field
intensity = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/NOV16-ch1.CSV",delimiter=",")
intensity2 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/1Rb87CH2.CSV",delimiter=",")
intensity = intensity[:,1]

# plt.plot(fit_voltage, intensity)



peaks = find_peaks(-intensity,height = 0.04,width=20)
peaks_small = find_peaks(intensity,height = -0.02,width=10)
# peak_pos = time[peaks[0]]
peak_field= time[peaks[0]]
magnetic_field = total_field[peaks[0]]
print(magnetic_field)

height = intensity[peaks[0]]
height2 = intensity[peaks_small[0]]
peak_field2 = total_field[peaks_small[0]]
# plt.title(r"${}^{87}$Rb")
plt.text(0.38, 0.05, r'F = 2, $m_{F}: 1 \longleftrightarrow 2$', fontsize = 12,transform=plt.gca().transAxes)
plt.text(0.29, 0.39, r'F = 2, $m_{F}: 0 \longleftrightarrow 1$', fontsize = 12,transform=plt.gca().transAxes)
# plt.text(0.3, 0.45, r'F = 2, $m_{F}: -1 \longleftrightarrow 0$', fontsize = 10,transform=plt.gca().transAxes)
plt.text(0.15, 0.57, r'F = 2, $m_{F}: -1 \longleftrightarrow 0$', fontsize = 12,transform=plt.gca().transAxes)
plt.text(0.01, 0.71, r'F = 2, $m_{F}: -2 \longleftrightarrow -1$', fontsize = 12,transform=plt.gca().transAxes)
plt.text(0.005, 0.92, r'F = 1, $m_{F}: 1 \longleftrightarrow 0$', fontsize = 12,transform=plt.gca().transAxes)
plt.text(0.4, 0.92, r'F = 1, $m_{F}: 0 \longleftrightarrow -1$', fontsize = 12,transform=plt.gca().transAxes)
plt.annotate('Arrows', xy=(0.1, .1), xytext=(0.5, 0.5),
            arrowprops=dict(arrowstyle='<->', color='red',transform=plt.gca().transAxes))


plt.plot(total_field,intensity)
plt.scatter(magnetic_field, height, color = 'r',s=10)
plt.scatter(peak_field2, height2, color = 'r',s=10)
plt.ylabel("Voltage (V)",fontsize = 16)
plt.xlabel("Magnetic Field (Gauss)",fontsize = 16)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.savefig('87.pdf',bbox_inches='tight')  
plt.show()
