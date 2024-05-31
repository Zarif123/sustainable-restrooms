import numpy as np
import pydub
from sklearn.preprocessing import MinMaxScaler
import argparse

def quantize(audio_signal, bits):
    bit_range = (0, (2**bits)-1)
    scaler = MinMaxScaler(feature_range=bit_range)

    # Quantize to 2 bits (0, 1, 2, 3)
    # Map normalized data to 2-bit integers (0, 1, 2, 3)
    quantized_signal = scaler.fit_transform(audio_signal.reshape(-1, 1))
    
    # Clip values to ensure they are within the valid range [0, 3]
    quantized_signal = np.clip(quantized_signal, 0, (2**bits)-1)

    return quantized_signal

def read(f, ext):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_file(f, ext)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    return a.frame_rate, y
    

def write(f, sr, x, ext="mp3"):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    y = np.int8(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format=ext)

def quantize_read_write(input_file, output, output_file_extension='wav', bits=1):
    input_broken = input_file.split("/")[-1].split(".")
    input_name = input_broken[0]
    input_ext = input_broken[1]

    # original_out = f'{output}/original_signal_{input_name}.out'
    # quantized_out = f'{output}/quantized_signal_{bits}_{input_name}.out'
    output_file_name = f'{output}/{input_name}_quant_{bits}.{output_file_extension}'

    frame_rate, audio_signal = read(input_file, input_ext)
    # np.savetxt(original_out, audio_signal, delimiter=',')

    quantized_signal = quantize(audio_signal, bits).astype(np.int8)
    # np.savetxt(quantized_out, quantized_signal, delimiter=',', fmt="%i")

    write(output_file_name, frame_rate, quantized_signal, output_file_extension)

    return output_file_name

desc_msg = "Quantize audio files to desire bit rate"

def main(): 
    parser = argparse.ArgumentParser(description=desc_msg)

    parser.add_argument("input_file", help="Audio input file")
    parser.add_argument("output_loc", help="Directory for output file")
    parser.add_argument("-e", nargs="?", default="wav", const="wav", help="Output audio extension (default: wav)")
    parser.add_argument("-b", nargs="?", default=1, const=1, help="Bits to quantize to file to (default: 1)")

    args = parser.parse_args()

    input = args.input_file
    output = args.output_loc
    output_ext = args.e

    try: 
        num_bits = int(args.b)
    except ValueError:
        raise ValueError("The provided bits value cannot be converted to an integer.")

    quantize_read_write(input_file=input, output=output, output_file_extension=output_ext, bits=num_bits)

if __name__=="__main__": 
    main() 