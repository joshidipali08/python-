#d.	Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500                  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs) # Time vector (1 second duration)

# Generate the original 10 Hz sine wave
original = np.sin(2 * np.pi * 10 * t)

# Scale the amplitude by a factor of 3
scaled = 3 * original

# Plot both signals
plt.figure(figsize=(10,5))
plt.plot(t, original, label='Original 10 Hz Sine Wave')
plt.plot(t, scaled, label='Scaled (Amplitude ×3)', linestyle='--')

plt.title('10 Hz Sine Wave - Original vs Scaled')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
