import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

# 1. Load audio + impulse response
audio_file = "C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav"
impulse_file = "C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav"

x, sr1 = sf.read(audio_file)
h, sr2 = sf.read(impulse_file)

# If stereo → convert to mono
if len(x.shape) > 1:
    x = x.mean(axis=1)
if len(h.shape) > 1:
    h = h.mean(axis=1)

# Check sampling rate
if sr1 != sr2:
    print("Warning: Sampling rates differ!")

# 2. Linear Convolution
linear_conv = fftconvolve(x, h, mode='full')

# 3. Circular Convolution
N = len(x) + len(h) - 1
X = np.fft.fft(x, N)
H = np.fft.fft(h, N)
circular_conv = np.fft.ifft(X * H).real

# 4. Visualization
plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.title("Original Audio Signal")
plt.plot(x)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.title("Linear Convolution Output")
plt.plot(linear_conv)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.title("Circular Convolution Output")
plt.plot(circular_conv)
plt.grid(True)

plt.tight_layout()
plt.show()

# 5. Save results (optional)
sf.write("linear_output.wav", linear_conv, sr1)
sf.write("circular_output.wav", circular_conv, sr1)

print("Processing complete. Files saved.")
