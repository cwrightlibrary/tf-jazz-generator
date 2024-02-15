import glob, pathlib
import pretty_midi
from music21 import *

data_dir = pathlib.Path.cwd().joinpath("mids")
filenames = glob.glob(str(data_dir.joinpath("*.mid")))

test_file = filenames[1]
save_file = pathlib.Path.cwd().joinpath("new_files")

midi_data = pretty_midi.PrettyMIDI(test_file)

def remove_instrument(input_midi_file, output_midi_file, instrument_numbers):
    midi_file = midi.MidiFile()
    midi_file.open(input_midi_file)
    midi_file.read()
    midi_file.close()
    
    for i in range(len(midi_file.tracks)):
        for event in midi_file.tracks[i].events:
            if "channel" in dir(event) and not event.channel in instrument_numbers:
                midi_file.tracks[i].events.remove(event)
    
    midi_file.open(output_midi_file, "wb")
    midi_file.write()
    midi_file.close()

instrument_numbers = [0, 1, 2, 24, 25, 26, 27, 28, 80, 81, 82, 83, 84, 85, 86, 87]

for input_file in filenames:
    output = save_file.joinpath(filenames.index(input_file))
    remove_instrument(input_file, output)
