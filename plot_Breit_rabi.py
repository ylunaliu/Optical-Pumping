import numpy as np
import matplotlib.pyplot as plt 


Z = 87

mu  = 9.274009*10**(-24)
h = 6.626068*10**(-34)

if Z==85:
    I = 5/2
    W = h*3035.735*10**6
    g_I = -0.000293640

else:
    I = 3/2
    W = h*3035.735*10**6
    g_I = -0.0009951414


g_l = 1
g_s = 2
S = 1/2
L=0
J=1/2

g_J = g_l*(J*(J+1) + L*(L+1) - S*(S+1))/(2*J*(J+1)) + g_s*(J*(J+1) - L*(L+1) + S*(S+1))/(2*J*(J+1))

Bfield = np.linspace(0,0.8,5000)

cases = np.array([1/2,-1/2])


for j in range(2):
    F = int(I + cases[j])
    print(F)
    g_F = g_J*(F*(F+1) + J*(J+1) - I*(I+1))/(2*F*(F+1)) + g_I*(F*(F+1) + I*(I+1) - J*(J+1))/(2*F*(F+1))
    print(g_F)

    Energies = np.zeros((int(2*F+1),len(Bfield)))
    m = np.linspace(-int(F),int(F),int(2*F+1))
    for i in range(len(Bfield)):
        x = (g_J - g_I)*mu*Bfield[i]/W

        first = -W/(2*(2*I+1)) + mu*g_I*Bfield[i]*m
        second = (W/2)*np.sqrt(1 + 4*m*x/(2*I + 1) + x**2)


        if j==1:
            second[0] = (W/2)*(1-x)
        
        E2_plus = np.empty((len(second), len(Bfield)))
        # print(np.shape(E2_plus))
        # print(np.shape(first+second))

        if j ==1:
            E2_plus[:,i] = first + second
            print(E2_plus)
        E2_minus = np.empty((len(second), len(Bfield)))
        if j ==2:
            E2_minus[:,i] = first - second
        # print(np.shape(second))

    print(np.shape(E2_plus))
    freq_shift_plus = E2_plus/h*10**-6
    freq_shift_minus = E2_minus/h*10**-6
    print(np.shape(freq_shift_plus))
plt.plot(Bfield, freq_shift_plus[1], '.')
plt.plot(Bfield, freq_shift_plus[2], '.')
plt.plot(Bfield, freq_shift_plus[0], '.')
plt.plot(Bfield, freq_shift_minus[0], '.')
plt.plot(Bfield, freq_shift_minus[1], '.')
plt.plot(Bfield, freq_shift_minus[2], '.')
# plt.plot(Bfield, freq_shift_plus[3], '.')
# plt.plot(Bfield, freq_shift_plus[4], '.')
    # # plt.plot(Bfield, freq_shift_plus[2])
    # # plt.plot(Bfield, freq_shift_minus[0])
    # # plt.plot(Bfield, freq_shift_minus[1]) 
plt.show()

    
