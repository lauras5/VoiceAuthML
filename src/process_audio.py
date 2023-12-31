import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from logging_config import logger
from paths import AUDIO_PATH

def process_audio_file(audio_file):
    try:
        # Load the audio file
        y, sr = librosa.load(audio_file, dtype=np.float32)
        # Extract audio features (e.g., MFCCs)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

        # Display the audio waveform and MFCCs
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        librosa.display.waveshow(y, sr=sr)
        plt.title('Audio Waveform')

        plt.subplot(2, 1, 2)
        librosa.display.specshow(mfccs, x_axis='time')
        plt.colorbar(format='%+2.0f dB')
        plt.title('MFCCs')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error: {str(e)}", exc_info=True)


if __name__ == "__main__":
    recorded_audio_file = f"{AUDIO_PATH}recorded_audio_20230911_1655.wav"
    process_audio_file(recorded_audio_file)
