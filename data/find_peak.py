import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

test = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/data/TEK0001.CSV",delimiter=",")
print(test[:,1])
plt.plot(test[:,0],test[:,1],'.')
plt.show()

# x = voltage[start:stop,0]
# voltage1 = voltage[start:stop,1]

# frequency = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0002.CSV",delimiter=",")
# frequency = frequency[, 0]
# xf = frequency[start:stop,1]
# start = 1000#680
# stop = len(frequency) -700

# peaks = find_peaks(-frequency,height = 0)
# peak_pos = x[peaks[0]]
# # peak_voltage = voltage1[peaks[0]]
# peak_time = xf[peaks[0]]
# # height = -frequency[peaks[0]]
# plt.scatter(peak_pos, height, color = 'r')
# print(peak_pos)
# print(peak_time)
# plt.plot(x, -frequency, 'b-')
# plt.plot(x, voltage1, 'k.')
# # plt.plot(x, -frequency, 'b.')
# # plt.title("Calibration field")
# plt.show()