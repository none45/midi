from mido import MidiFile, MidiTrack, MetaMessage

playlist_path = "midis/playlist.txt"
output_path = "midis/playlist.mid"

with open(playlist_path, "r") as f:
    midi_paths = [line.strip() for line in f.readlines() if line.strip()]

combined = MidiFile()
ticks_per_beat = combined.ticks_per_beat

master_track = MidiTrack()
combined.tracks.append(master_track)

master_track.append(MetaMessage('set_tempo', tempo=500000, time=0))

for path in midi_paths:
    m = MidiFile(path)
    
    master_track.append(MetaMessage('marker', text=f'Start {path}', time=0))

    for t in m.tracks:
        new_track = MidiTrack()
        combined.tracks.append(new_track)

        for msg in t:
            new_track.append(msg.copy(time=msg.time))

combined.save(output_path)
print("Merged MIDI saved:", output_path)
