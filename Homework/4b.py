import numpy as np
import matplotlib.pyplot as plt
import random

# (b1) Plot the parametric curve for specific values of R, δr, f, and p
theta = np.linspace(0, 2*np.pi, 500)  # theta ranging from 0 to 2π

# Parameters for the first curve
R = 1.2
delta_r = 0.1
f = 15
p = 0

# Parametric equations
x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

# Plot the first curve
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title('Wavy Circle (R=1.2, δr=0.1, f=15, p=0)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

# (b2) Plot 10 curves with R = i, δr = 0.05, f = 2 + i, p as a random number

plt.figure(figsize=(6, 6))

for i in range(1, 11):
    R = i
    delta_r = 0.05
    f = 2 + i
    p = random.uniform(0, 2*np.pi)  # random p value between 0 and 2π

    # Parametric equations for each curve
    x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

    plt.plot(x, y, label=f'R={i}, f={f:.2f}, p={p:.2f}')

plt.title('Wavy Circles with Random p')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
