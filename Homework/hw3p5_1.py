import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - 4 * np.sin(2 * x) - 3

# Plot the function
x_vals = np.linspace(-9, 9, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = x - 4sin(2x) - 3")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Plot of f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.text(-4.8,-14,"Function has five roots, no roots att x approx 7")
plt.grid(True)
plt.legend()
plt.show()
