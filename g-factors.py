import numpy as np
import uncertainties as uc
uncertainty =  0.0136
field_0 = 8.991*10**-3*11/(0.1639)*10**-5
print(field_0)
field_87 = 8.991*10**-3*11/(0.1639)*10**-5
field_85 = 8.991*10**-3*11/(0.1639)*10**-5
mu_B = 5.8*10**-5
h = 4.136*10**-15

Current_0 = uc.ufloat(0.304, uncertainty)
current_87 = uc.ufloat(0.544, uncertainty)
current_85 = uc.ufloat(0.672, uncertainty)

g_factor_87 = 10000*h/((current_87-Current_0)*field_87*mu_B)
print(g_factor_87)
print(field_0*(current_87-Current_0))

g_factor_85 = 10000*h/((current_85-Current_0)*field_85*mu_B)
print(g_factor_85)
print(0.682*8.991*10**-3*11/(0.1639))
# m_87 = uc.ufloat(m1, m1_err)
# print(m, m1)
# ratio = m_87/m_85
# print(ratio)