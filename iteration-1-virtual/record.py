import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import whisper
import datetime
import json

# Settings
duration = 5  # seconds
sample_rate = 44100  # Hz

# Get absolute path to the script's dir
base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir,"iteration-1-virtual","audio_samples")
filename = "sample_recording.wav"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Record audio
print(f"Recording for {duration} seconds...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()
print("Recording complete.")

# Save to file
output_path = os.path.join(output_dir, filename)
wav.write(output_path, sample_rate, audio)
print(f"Saved recording to: {output_path}")
