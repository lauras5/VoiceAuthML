# capture audio file from microphone
import pyaudio
import wave
import time
import sys

from logging_config import logger

# duration in seconds
def capture_audio_to_file(output_file, duration=5, sample_rate=44100, channels=1):
    audio = pyaudio.PyAudio()

    try:
        stream = audio.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=1024)

        print(f"Recording audio for {duration} seconds...")

        frames = []
        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # write to output wav file
        with wave.open(output_file, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

    except Exception as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error: {str(e)}")
        return False

    return True

# test
if __name__ == "__main__":
    timestr = time.strftime("%Y%m%d_%H%M")
    out_filename = f"../data/audio_samples/recorded_audio_{timestr}.wav"
    capture_audio_to_file(out_filename, duration=5)
