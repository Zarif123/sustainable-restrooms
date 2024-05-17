import os
from pathlib import Path
import sound

def delete_files(folder):
    delete_folder = f'training_set/{folder}'
    delete_path = Path.cwd()/f'{delete_folder}'
    for file in os.listdir(delete_path):
        delete_file = os.path.join(f'{delete_path}',file)
        if os.path.exists(delete_file):
            os.remove(delete_file)
    print(f'Done deleting {folder}')

def out_to_training(class_type, bits):
    out_path = Path.cwd()/'out'
    class_out_path = out_path/f'{class_type}'
    for file in os.listdir(class_out_path):
        input_file = os.path.join(f'out/{class_type}/',file)
        output_file = f'training_set/{class_type}'
        sound.quantize_read_write(input_file=input_file, output=output_file, output_file_extension='wav', bits=bits)
    print(f'Done converting {class_type}')
    
delete_files(folder='urination')
delete_files(folder='speech')
delete_files(folder='defecation')
delete_files(folder='noise')
delete_files(folder='silence')

out_to_training(class_type='urination', bits=2)
out_to_training(class_type='defecation', bits=2)
out_to_training(class_type='speech', bits=2)
out_to_training(class_type='noise', bits=2)
out_to_training(class_type='silence', bits=2)