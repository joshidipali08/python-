# # # 1
# # import soundfile as sf

# # # Load audio file
# # audio, sample_rate = sf.read('C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav')
# # # Write audio file
# # sf.write('new_audio_file.wav', audio, sample_rate)

# # # Load audio file
# # audio, sample_rate = sf.read('C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav')
# # # Write audio file
# # sf.write('new_audio_file.wav', audio, sample_rate)


##2

# import soundfile as sf

# # Load audio file
# audio, sample_rate = sf.read(r'C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav')


# # Write audio file
# sf.write('new_audio_file.wav', audio, sample_rate)

# import matplotlib.pyplot as plt
# import numpy as np
# import soundfile as sf
# # Load audio file
# #audio, sample_rate = sf.read('C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav')
# # Create time axis
# time = np.arange(0, len(audio)) / sample_rate
# # Plot audio signal
# plt.plot(time, audio)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()


##3
from pydub import AudioSegment

# Load audio file
audio = AudioSegment.from_file('C:/Users/jjosh/OneDrive/Desktop/pwp/HC PWP/lab 20/file_example_WAV_1MG.wav')

# Add fade in effect
audio_fade_in = audio.fade_in(2000)  # 2 seconds

# Export audio file with fade in effect
audio_fade_in.export('audio_file_fade_in.wav', format='wav')
