import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setting a theme
sns.set_theme(style="darkgrid")

# Example Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
sns.lineplot(x=x, y=y, label="Sine Wave", color="blue")
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
