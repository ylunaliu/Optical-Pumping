import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


voltage = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0003.CSV",delimiter=",")

start = 0#680
stop = len(voltage) - 0
x = voltage[start:stop,0]
voltage1 = voltage[start:stop,1]

frequency = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0002.CSV",delimiter=",")[start:stop,1]


peaks = find_peaks(-frequency, height=0.3)
peak_pos = x[peaks[0]]
peak_voltage = voltage1[peaks[0]]
height = -frequency[peaks[0]]
plt.scatter(peak_pos, height, color = 'r')
print(peak_pos)
print(peak_voltage)
plt.plot(x, voltage1, 'k.')
plt.plot(x, -frequency, 'b.')
# plt.title("Calibration field")
plt.show()