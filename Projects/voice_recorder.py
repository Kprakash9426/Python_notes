import sounddevice as sd
from scipy.io.wavfile import write

fs = 48000  # Windows works better with 48000 sometimes
duration = int(input("Enter time in seconds: "))

devices = sd.query_devices()
print(devices)

device_id = int(input("Enter microphone device ID: "))

print("Recording...")

record_voice = sd.rec(
    int(duration * fs),
    samplerate=fs,
    channels=1,
    dtype='int16',
    device=device_id
)

sd.wait()
write("out.wav", fs, record_voice)

print("Recording complete. Check out.wav")
