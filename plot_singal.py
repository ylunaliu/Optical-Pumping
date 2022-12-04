import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0021.csv",delimiter=",")

# current = np.loadtxt("/Users/luna/Documents/GitHub/Optical_pumpinh/TEK0019.csv",delimiter=",")


start = 0#680
stop = len(data) -0
x = data[start:stop,0]
# x1 = current[start:stop,0]

y = data[start:stop,1]
plt.figure(figsize=(8, 4))
# y1 = current[start:stop,1]
plt.ylabel("Voltage (V)", fontsize = 20)
plt.xlabel("Magnetic field (arb. unit)",fontsize = 20)
plt.yticks(fontsize=18)
plt.xticks(fontsize=18)
plt.plot(x,y)
plt.tight_layout()
# plt.plot(x1, y1)
plt.savefig('signal.pdf',bbox_inches='tight')  
plt.show()
