import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
# Position of the peaks for 87Rb for the last four large peak: [-0.0491 -0.0278  0.0021  0.0346], voltage = [ 9.   9.6 10.4 11.2]

main_field = 8.71*0.512*2


# test = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/Current_Nov7.CSV",delimiter=",")
# print(test[:,1])
# plt.plot(test[:,0],test[:,1],'.')
# plt.show()
voltage1 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/1Rb85CH1.CSV",delimiter=",")
print(np.shape(voltage1))
time =voltage1[:,0]
voltage = voltage1[:,1]
sweep_field = 0.618*voltage-0.19-6.4
print(voltage)
total_field = sweep_field+main_field
intensity = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/1Rb85CH2.CSV",delimiter=",")
intensity = intensity[:,1]
plt.plot(voltage, intensity)
plt.show()
peaks = find_peaks(-intensity,height = 0.36,width=20)
peaks_small = find_peaks(intensity,height = -0.325,width=20)
# peak_pos = time[peaks[0]]
peak_field= time[peaks[0]]
magnetic_field = total_field[peaks[0]]
print(magnetic_field)

height = intensity[peaks[0]]
height2 = intensity[peaks_small[0]]
peak_field2 = time[peaks_small[0]]
plt.title(r"${}^{85}$Rb")
plt.scatter(peak_field, height, color = 'r')
plt.scatter(peak_field2, height2, color = 'r')
plt.plot(time,intensity)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()