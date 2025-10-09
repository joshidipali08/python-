#e.	Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500                  # Sampling frequency (Hz)
t = np.arange(0, 2, 1/fs) # Time vector for 2 seconds

# Generate the original 5 Hz sine wave
original = np.sin(2 * np.pi * 5 * t)

# Reverse the signal in time
reversed_signal = original[::-1]

# Plot both signals
plt.figure(figsize=(10,5))
plt.plot(t, original, label='Original 5 Hz Sine Wave')
plt.plot(t, reversed_signal, label='Time-Reversed Signal', linestyle='--')

plt.title('5 Hz Sine Wave - Original vs Time-Reversed')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
