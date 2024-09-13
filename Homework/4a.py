import numpy as np

# (a) Create vector t and evaluate sum S
t = np.arange(0, np.pi + np.pi/30, np.pi/30)  # from 0 to pi with step size pi/30
y = np.cos(t)  # y = cos(t)

# Evaluate the sum S = sum(t(k) * y(k))
S = np.sum(t * y)

print(f"The sum is: {S}")
