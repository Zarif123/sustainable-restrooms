from pydub import AudioSegment

song = AudioSegment.from_mp3("out/number1/number_one_quantized_4.mp3")

i = 0
length = len(song)

while i*500 < length:
    if (i+1)*500 > length:
        break 
    else:
        awesome = song[500*i:500*(i+1)]
        awesome.export(f"training_set/mashup{i}.mp3", format="mp3")
    i += 1