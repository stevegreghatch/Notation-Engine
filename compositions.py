import noteFunctions

# Fur Elise Notes

# E E♭ E E♭ E
# B D C A
# A B
# G♯ B C
# E E♭ E E♭ E
# B D C A
# A B
# C B A

# E E♭ E E♭ E
# B D C A
# A B
# G♯ B C
# E E♭ E E♭ E
# B D C A
# A B
# C B A

# B C D E
# F E D
# E D C
# D C B

# E E♭ E E♭ E
# B D C A
# A B
# G♯ B C
# E E♭ E E♭ E
# B D C A
# A B
# C B A

furElise = [noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5,
            noteFunctions.B4, noteFunctions.D5, noteFunctions.C5, noteFunctions.A4,
            noteFunctions.A4, noteFunctions.B4,
            noteFunctions.Ab4, noteFunctions.B4, noteFunctions.C5,

            noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5,
            noteFunctions.B4, noteFunctions.D5, noteFunctions.C5, noteFunctions.A4,
            noteFunctions.A4, noteFunctions.B4,
            noteFunctions.C5, noteFunctions.B4, noteFunctions.A4,

            noteFunctions.B4, noteFunctions.C5, noteFunctions.D5, noteFunctions.E5,
            noteFunctions.F5, noteFunctions.E5, noteFunctions.D5,
            noteFunctions.E5, noteFunctions.D5, noteFunctions.C5,
            noteFunctions.D5, noteFunctions.C5, noteFunctions.B4,

            noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5, noteFunctions.Eb5, noteFunctions.E5,
            noteFunctions.B4, noteFunctions.D5, noteFunctions.C5, noteFunctions.A4,
            noteFunctions.A4, noteFunctions.B4,
            noteFunctions.C5, noteFunctions.B4, noteFunctions.A4]


def playFurElise():
    playback = []
    for note in furElise:
        playback.append(note())
