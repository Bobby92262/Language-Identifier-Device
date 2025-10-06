import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import whisper
import datetime
import json

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONFIGURATION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DURATION = 5 # Recording duration in seconds
SAMPLE_RATE = 44100 # Audio sample rate in Hz
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audio_samples")
MODEL_NAME = "base" # Whisper model size: tiny,base,small,mdeium,large
LOG_FILE = os.path.join(AUDIO_DIR, "transcription_log.json")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def record_audio(filename: str) -> str:
    """
    Records auio from the default input device and saves it as a WAV file.

    Args:
        filename (str): Name of the output WAV file
    
    Returns:
        str: Full path to the saved audio file.
    """
    os.makedirs(AUDIO_DIR, exist_ok=True)
    output_path = os.path.join(AUDIO_DIR, filename)

    print(f"[INFO] Recording for {DURATION} seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    wav.write(output_path, SAMPLE_RATE, audio)
    print(f"[INFO] Saved recording to: {output_path}")
    return output_path

def transcribe_audio(file_path: str) -> dict:
    """
    Transcribes the given audio file using OpenAI Whisper.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        dict: Transcription result including text and detected language.
    """
    print(f"[INFO] Loading Whisper model: {MODEL_NAME}")
    model = whisper.load_model(MODEL_NAME)
    result = model.transcribe(file_path)
    print(f"[INFO] Transcription complete. Detected language: {result['language']}")
    return result

def log_transcription(filename: str, result: dict):
    """
    Logs transcription metadata to a JSON file.

    Args:
        filename (str): Name of the audio file
        result (dict): Transcription result from Whisper
    """
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "filename": filename,
        "language": result["language"],
        "text": result["text"]
    }

    # Load exisitng log or initialize
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"[INFO] Logged transcription to: {LOG_FILE}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN EXECUTION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    #Generate timestamped filename
    timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"sample_recording_{timestamp}.wav"

    #Record, transcribe, and log
    audio_path = record_audio(filename)
    result = transcribe_audio(audio_path)
    log_transcription(filename, result)