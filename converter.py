import sound 
import audio_segment 

input = sound.quantize_read_write(input_file="audio/speech/speech_1.mp3", output="out/speech", output_file_extension="wav", bits=3)
audio_segment.process(input, "training_set", 500)