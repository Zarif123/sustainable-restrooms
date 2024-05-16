import os
from pathlib import Path
import sound

out_path = Path.cwd()/'out'
urination_out_path = out_path/'urination'

for file in os.listdir(urination_out_path):
    input_file = os.path.join(f'out/urination/',file)
    output_file = 'training_set/urination'
    sound.quantize_read_write(input_file=input_file, output=output_file, output_file_extension='wav', bits=3)