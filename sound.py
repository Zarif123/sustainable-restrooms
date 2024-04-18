import numpy as np
import pydub
from sklearn.preprocessing import StandardScaler

def quantize(audio_signal):
    scaler = StandardScaler()
    # quantized_signal = np.where(audio_signal < 0, 1, 0)
    
    # Step 3: Quantize to 2 bits (0, 1, 2, 3)
    # Map normalized data to 2-bit integers (0, 1, 2, 3)
    quantized_signal = scaler.fit_transform(audio_signal.reshape(-1, 1))
    
    # Clip values to ensure they are within the valid range [0, 3]
    quantized_signal = np.clip(quantized_signal, 0, 3)

    return quantized_signal

def read(f, normalized=False):
    scaler = StandardScaler()
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, scaler.fit_transform(y)
    else:
        return a.frame_rate, y
    

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int8(x * 2 ** 15)
    else:
        y = np.int8(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3")

input_file_name = 'number_one'
input_file_extension = '.mp3'
original_out = f'original_signal_{input_file_name}.out'
quantized_out = f'quantized_signal_{input_file_name}.out'
output_file_name = f'{input_file_name}_quantized{input_file_extension}'

_, audio_signal = read(input_file_name + input_file_extension, normalized=False)
np.savetxt(original_out, audio_signal, delimiter=',')
quantized_signal = quantize(audio_signal).astype(np.int8)
np.savetxt(quantized_out, quantized_signal, delimiter=',', fmt="%i")

write(output_file_name, 24000, quantized_signal, normalized=False)