import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

CH1 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/data/Nov16CH1.csv",delimiter=",")
CH2 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/data/Nov16CH2.CSV",delimiter=",")

plt.plot(CH1[:,0], CH1[:,1])
plt.plot(CH2[:,0], CH2[:,1])
plt.show()
print(CH2[:,1])
# start = 680#
# stop = len(data)-800
# x = data[start:stop,0]
# y = data[start:stop,1]


data2 = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/data/TEK0001.csv",delimiter=",")
calibrate_field = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/data/TEK0002.csv",delimiter=",")

x3 = calibrate_field[start:stop,0]
y3 = calibrate_field[start:stop,1]

x1 = data2[start:stop,0]
y1 = data2[start:stop,1]
m=1
b = 0
g = m*y3+b

plt.plot(x3,y3, '.')
# plt.plot(x,y)
plt.plot(x1,y1,'r', label = "y = {:.3f}x + {:.2f}".format(m,b))
plt.show()