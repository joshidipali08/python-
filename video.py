import moviepy
from tkinter.filedialog import *

vi = askopenfilename()
video = moviepy.VideoFileClip(vi)

aud = video.audio

save_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
aud.write_audiofile(save_path)

print("----end---")

