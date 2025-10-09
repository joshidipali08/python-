import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500                 # Sampling frequency (Hz)
t = np.arange(0, 2, 1/fs)  # Time vector (2 seconds)

# Generate the original 5 Hz sine wave
original = np.sin(2 * np.pi * 5 * t)

# Generate the shifted version (delay of 0.1 seconds)
shifted = np.sin(2 * np.pi * 5 * (t - 0.1))

# Plot both signals
plt.figure(figsize=(10,5))
plt.plot(t, original, label='Original 5 Hz Sine Wave')
plt.plot(t, shifted, label='Shifted (0.1 s delay)', linestyle='--')

plt.title('5 Hz Sine Wave - Original vs Time-Shifted')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
