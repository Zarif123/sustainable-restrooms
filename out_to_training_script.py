import os
from pathlib import Path
import sound

def out_to_training(class_type):
    out_path = Path.cwd()/'out'
    class_out_path = out_path/f'{class_type}'
    for file in os.listdir(class_out_path):
        input_file = os.path.join(f'out/{class_type}/',file)
        output_file = f'training_set/{class_type}'
        sound.quantize_read_write(input_file=input_file, output=output_file, output_file_extension='wav', bits=3)
    print("Done")
    
out_to_training('defecation')