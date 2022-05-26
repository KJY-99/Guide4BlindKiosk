import argparse


def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('filename', help='audio file to be played back')
parser.add_argument('-d', '--device', type=int_or_str,
                    help='output device (numeric ID or substring)')
args = parser.parse_args()

try:
    import sounddevice as sd
    import soundfile as sf
    import numpy
    assert numpy
    
    data, fs = sf.read(args.filename, dtype='float32')
    sd.play(data, fs, device=args.device)
    status = sd.wait()
    duration = 10.5  # seconds
    myarray = sd.rec(int(duration * fs), samplerate=fs, channels=2)    
    myrecording = sd.playrec(myarray, fs, channels=2)
    status = sd.wait()
    if status:
        parser.exit('Error during playback: ' + str(status))
except KeyboardInterrupt:
    parser.exit('\nInterrupted by user')
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
