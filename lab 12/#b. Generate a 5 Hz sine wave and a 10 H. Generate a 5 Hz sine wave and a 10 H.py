#b.	Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500        # Sampling frequency (Hz)
t = np.arange(0, 2, 1/fs)   # Time vector for 2 seconds

# Generate signals
sine_wave = np.sin(2 * np.pi * 5 * t)    # 5 Hz sine wave
cosine_wave = np.cos(2 * np.pi * 10 * t) # 10 Hz cosine wave

# Multiply element-wise
result = sine_wave * cosine_wave

# Plot all signals
plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(t, sine_wave)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3,1,2)
plt.plot(t, cosine_wave)
plt.title('10 Hz Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3,1,3)
plt.plot(t, result)
plt.title('Result of Element-wise Multiplication')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
