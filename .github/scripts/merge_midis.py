from mido import MidiFile, MidiTrack

playlist_path = "midis/playlist.txt"
output_path = "midis/playlist.mid"

with open(playlist_path, "r") as f:
    midi_paths = [line.strip() for line in f.readlines() if line.strip()]

combined = MidiFile()
track = MidiTrack()
combined.tracks.append(track)

for path in midi_paths:
    m = MidiFile(path)
    for msg in m.tracks[0]:
        track.append(msg)

combined.save(output_path)

print("Merged MIDI saved:", output_path)
