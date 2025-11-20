#use Python to implement both cross-correlation and autocorrelation on a set of audio files (clean_audio.wav, noisy_audio.wav, periodic_audio.wav). Visualize and compare the results.
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import correlate

# 1. Load audio files
clean_file = "C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav"
noisy_file = "C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav"
periodic_file = "C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav"

clean, sr1 = sf.read(clean_file)
noisy, sr2 = sf.read(noisy_file)
periodic, sr3 = sf.read(periodic_file)

# Convert to mono if stereo
if len(clean.shape) > 1:
    clean = clean.mean(axis=1)
if len(noisy.shape) > 1:
    noisy = noisy.mean(axis=1)
if len(periodic.shape) > 1:
    periodic = periodic.mean(axis=1)

# 2. Autocorrelation Function
def autocorr(x):
    return correlate(x, x, mode='full')

auto_clean = autocorr(clean)
auto_noisy = autocorr(noisy)
auto_periodic = autocorr(periodic)

# 3. Cross-Correlation
cross_clean_noisy = correlate(clean, noisy, mode='full')
cross_clean_periodic = correlate(clean, periodic, mode='full')
cross_noisy_periodic = correlate(noisy, periodic, mode='full')

# 4. Visualization
plt.figure(figsize=(16, 12))

plt.subplot(3, 2, 1)
plt.title("Autocorrelation - Clean Audio")
plt.plot(auto_clean)
plt.grid(True)

plt.subplot(3, 2, 3)
plt.title("Autocorrelation - Noisy Audio")
plt.plot(auto_noisy)
plt.grid(True)

plt.subplot(3, 2, 5)
plt.title("Autocorrelation - Periodic Audio")
plt.plot(auto_periodic)
plt.grid(True)

plt.subplot(3, 2, 2)
plt.title("Cross-Correlation: Clean ↔ Noisy")
plt.plot(cross_clean_noisy)
plt.grid(True)

plt.subplot(3, 2, 4)
plt.title("Cross-Correlation: Clean ↔ Periodic")
plt.plot(cross_clean_periodic)
plt.grid(True)

plt.subplot(3, 2, 6)
plt.title("Cross-Correlation: Noisy ↔ Periodic")
plt.plot(cross_noisy_periodic)
plt.grid(True)

plt.tight_layout()
plt.show()

print("Processing complete.")
