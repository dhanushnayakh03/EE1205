import numpy as np
import matplotlib.pyplot as plt

# Load data from the txt file
data = np.loadtxt("data.txt", skiprows=1)

# Extract the data
time = data[:, 0]
q = data[:, 1]
i = data[:, 2]
L = 50e-6
C = 50e-6


# Plotting Q(t)
plt.figure(figsize=(8, 6))
plt.plot(time, q, label='Charge on Capacitor', linestyle='-', color='blue', linewidth=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)


plt.xlabel('Time (s)')
plt.ylabel('Charge (Coulombs)')
plt.title('Charge on Capacitor as a Function of Time')
plt.legend(loc='upper left')
plt.grid(True)
plt.savefig("charge_plot.png")

plt.clf()

# Plotting I(t)
plt.figure(figsize=(8, 6))
plt.plot(time, i, label='Inductor Current', linestyle='-', color='red', linewidth=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.xlabel('Time (s)')
plt.ylabel('Current (Amperes)')
plt.title('Inductor Current as a Function of Time')
plt.legend(loc ='upper left')
plt.grid(True)
plt.savefig("current_plot.png")
plt.show()
plt.clf()
