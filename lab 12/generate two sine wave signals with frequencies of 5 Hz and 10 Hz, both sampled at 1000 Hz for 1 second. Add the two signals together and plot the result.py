#a.	Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.
import numpy as np
print(np.__version__)
import matplotlib.pyplot as plt

# Parameters
fs = 1000          # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Time from 0 to 1 sec (1000 samples)

# Generate two sine waves
f1 = 5   # Frequency of first sine wave
f2 = 10  # Frequency of second sine wave

sine1 = np.sin(2 * np.pi * f1 * t)
sine2 = np.sin(2 * np.pi * f2 * t)

# Add the two signals
sum_signal = sine1 + sine2

# Plot the signals
plt.figure(figsize=(12, 8))

# 5 Hz Sine Wave
plt.subplot(3, 1, 1)
plt.plot(t, sine1)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# 10 Hz Sine Wave
plt.subplot(3, 1, 2)
plt.plot(t, sine2)
plt.title('10 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Sum of Both Sine Waves
plt.subplot(3, 1, 3)
plt.plot(t, sum_signal)
plt.title('Sum of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
