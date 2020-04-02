import matplotlib.pyplot as plt
import numpy as np

A = 101325
P = 4650
T = 44.5

# Alpha-Beta
P_ab = 1
T_ab = 36

S_1 = 4.59
V_1 = 0.043 * 10 ** (-6)

B_1 = (P - P_ab) / np.log(T / T_ab)
C_1 = P_ab - B_1 * np.log(T_ab)

T_1 = np.linspace(36, T)
P_1 = B_1 * np.log(T_1) + C_1

# Alpha-Gamma
S_2 = 1.25
V_2 = 0.165 * 10 ** (-6)

B_2 = S_2 / V_2 / A
C_2 = P - B_2 * T

T_2 = np.linspace(0, T)
P_2 = B_2 * T_2 + C_2

# Gamma-Beta
S_3 = S_1 + S_2
V_3 = V_2 + V_2

B_3 = S_3 / V_3 / A
C_3 = P - B_3 * T

T_3 = np.linspace(T, 70)
P_3 = B_3 * T_3 + C_3

# Plot
plt.plot(T_1,P_1)
plt.plot(T_2,P_2)
plt.plot(T_3,P_3)

plt.title('Nitrogen Phase Diagram')
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (atm)')

plt.text(17, 1000, 'Alpha')
plt.text(55, 3000, 'Beta')
plt.text(20, 6000, 'Gamma')