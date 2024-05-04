from pydub import AudioSegment
import argparse

def process(input, output, ms=1000):
    input_name = input.split("/")[-1].split(".")[0]
    song = AudioSegment.from_mp3(input)

    i = 0
    length = len(song)

    # 1000 equals 1 second
    while i*ms < length:
        if (i+1)*ms > length:
            break 
        else:
            slice = song[ms*i:ms*(i+1)]
            slice.export(f"{output}/{input_name}_{i}.wav", format="wav")
        i += 1

desc_msg = "Segment audio files by millisecond"

def main(): 
    parser = argparse.ArgumentParser(description=desc_msg)

    parser.add_argument("input_file", help="Audio input file")
    parser.add_argument("output_loc", help="Directory for output files")
    parser.add_argument("-t", nargs="?", default=1000, const=1000, help="Length of segmented audio file in milliseconds (default: 1000)")

    args = parser.parse_args()

    input = args.input_file
    output = args.output_loc
    
    try: 
        ms = int(args.t)
    except ValueError:
        raise ValueError("The provided bits value cannot be converted to an integer.")
    
    process(input, output, ms)

if __name__=="__main__": 
    main() 