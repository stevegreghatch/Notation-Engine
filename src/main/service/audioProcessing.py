from music21 import stream, note


def create_sheet_music(pitches):
    s = stream.Stream()
    for pitch in pitches:
        n = note.Note()
        n.pitch.midi = pitch
        s.append(n)
    return s
