from pydub import AudioSegment

audio = AudioSegment.from_file("shit.m4a", "m4a")
audio.export("shit.wav", format="wav")