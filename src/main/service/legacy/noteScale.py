import noteFunctions

# All Notes  --------------------------------------------------------------------------------------------------------

listOfNoteNamesInCMajorScale = []
listOfNoteNamesInDMajorScale = []
listOfNoteNamesInEMajorScale = []
listOfNoteNamesInFMajorScale = []
listOfNoteNamesInGMajorScale = []
listOfNoteNamesInAMajorScale = []
listOfNoteNamesInBMajorScale = []

allNotes = [noteFunctions.D1, noteFunctions.Eb1, noteFunctions.E1, noteFunctions.F1,
            noteFunctions.Gb1, noteFunctions.G1, noteFunctions.Ab1, noteFunctions.A1,
            noteFunctions.Bb1, noteFunctions.B1,

            noteFunctions.C2, noteFunctions.D2, noteFunctions.Eb2, noteFunctions.E2,
            noteFunctions.F2, noteFunctions.Gb2, noteFunctions.G2, noteFunctions.Ab2,
            noteFunctions.A2, noteFunctions.Bb2, noteFunctions.B2,

            noteFunctions.C3, noteFunctions.D3, noteFunctions.Eb3, noteFunctions.E3,
            noteFunctions.F3, noteFunctions.Gb3, noteFunctions.G3, noteFunctions.Ab3,
            noteFunctions.A3, noteFunctions.Bb3, noteFunctions.B3,

            noteFunctions.C4, noteFunctions.D4, noteFunctions.Eb4, noteFunctions.E4,
            noteFunctions.F4, noteFunctions.Gb4, noteFunctions.G4, noteFunctions.Ab4,
            noteFunctions.A4, noteFunctions.Bb4, noteFunctions.B4,

            noteFunctions.C5, noteFunctions.D5, noteFunctions.Eb5, noteFunctions.E5,
            noteFunctions.F5, noteFunctions.Gb5, noteFunctions.G5, noteFunctions.Ab5,
            noteFunctions.A5, noteFunctions.Bb5, noteFunctions.B5,

            noteFunctions.C6, noteFunctions.D6, noteFunctions.Eb6, noteFunctions.E6,
            noteFunctions.F6, noteFunctions.Gb6, noteFunctions.G6, noteFunctions.Ab6,
            noteFunctions.A6, noteFunctions.Bb6, noteFunctions.B6,

            noteFunctions.C7, noteFunctions.D7, noteFunctions.Eb7, noteFunctions.E7,
            noteFunctions.F7, noteFunctions.Gb7, noteFunctions.G7, noteFunctions.Ab7,
            noteFunctions.A7, noteFunctions.Bb7, noteFunctions.B7,

            noteFunctions.C8, noteFunctions.D8, noteFunctions.Eb8, noteFunctions.E8,
            noteFunctions.F8, noteFunctions.Gb8, noteFunctions.G8, noteFunctions.Ab8,
            noteFunctions.A8, noteFunctions.Bb8, noteFunctions.B8]

# Major Scales --------------------------------------------------------------------------------------------------------
# C Major

CMajor1Scale = [noteFunctions.D1, noteFunctions.E1, noteFunctions.F1, noteFunctions.G1,
                noteFunctions.A1, noteFunctions.B1, noteFunctions.C2]
CMajor2Scale = [noteFunctions.C2, noteFunctions.D2, noteFunctions.E2, noteFunctions.F2,
                noteFunctions.G2, noteFunctions.A2, noteFunctions.B2, noteFunctions.C3]
CMajor3Scale = [noteFunctions.C3, noteFunctions.D3, noteFunctions.E3, noteFunctions.F3,
                noteFunctions.G3, noteFunctions.A3, noteFunctions.B3, noteFunctions.C4]
CMajor4Scale = [noteFunctions.C4, noteFunctions.D4, noteFunctions.E4, noteFunctions.F4,
                noteFunctions.G4, noteFunctions.A4, noteFunctions.B4, noteFunctions.C5]
CMajor5Scale = [noteFunctions.C5, noteFunctions.D5, noteFunctions.E5, noteFunctions.F5,
                noteFunctions.G5, noteFunctions.A5, noteFunctions.B5, noteFunctions.C6]
CMajor6Scale = [noteFunctions.C6, noteFunctions.D6, noteFunctions.E6, noteFunctions.F6,
                noteFunctions.G6, noteFunctions.A6, noteFunctions.B6, noteFunctions.C7]
CMajor7Scale = [noteFunctions.C7, noteFunctions.D7, noteFunctions.E7, noteFunctions.F7,
                noteFunctions.G7, noteFunctions.A7, noteFunctions.B7, noteFunctions.C8]
CMajor8Scale = [noteFunctions.C8, noteFunctions.D8, noteFunctions.E8, noteFunctions.F8,
                noteFunctions.G8, noteFunctions.A8, noteFunctions.B8]

CMajor1ScaleArpeggio = [noteFunctions.E1, noteFunctions.G1, noteFunctions.C2]
CMajor2ScaleArpeggio = [noteFunctions.C2, noteFunctions.E2, noteFunctions.G2,
                        noteFunctions.C3]
CMajor3ScaleArpeggio = [noteFunctions.C3, noteFunctions.E3, noteFunctions.G3,
                        noteFunctions.C4]
CMajor4ScaleArpeggio = [noteFunctions.C4, noteFunctions.E4, noteFunctions.G4,
                        noteFunctions.C5]
CMajor5ScaleArpeggio = [noteFunctions.C5, noteFunctions.E5, noteFunctions.G5,
                        noteFunctions.C6]
CMajor6ScaleArpeggio = [noteFunctions.C6, noteFunctions.E6, noteFunctions.G6,
                        noteFunctions.C7]
CMajor7ScaleArpeggio = [noteFunctions.C7, noteFunctions.E7, noteFunctions.G7,
                        noteFunctions.C8]
CMajor8ScaleArpeggio = [noteFunctions.C8, noteFunctions.E8, noteFunctions.G8]

CMajorFullScale = CMajor1Scale + CMajor2Scale + CMajor3Scale + CMajor4Scale + CMajor5Scale + CMajor6Scale + \
                  CMajor7Scale + CMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# D Major

DMajor1Scale = [noteFunctions.D1, noteFunctions.E1, noteFunctions.Gb1, noteFunctions.G1,
                noteFunctions.A1, noteFunctions.B1, noteFunctions.Db2, noteFunctions.D2]
DMajor2Scale = [noteFunctions.D2, noteFunctions.E2, noteFunctions.Gb2, noteFunctions.G2,
                noteFunctions.A2, noteFunctions.B2, noteFunctions.Db3, noteFunctions.D3]
DMajor3Scale = [noteFunctions.D3, noteFunctions.E3, noteFunctions.Gb3, noteFunctions.G3,
                noteFunctions.A3, noteFunctions.B3, noteFunctions.Db4, noteFunctions.D4]
DMajor4Scale = [noteFunctions.D4, noteFunctions.E4, noteFunctions.Gb4, noteFunctions.G4,
                noteFunctions.A4, noteFunctions.B4, noteFunctions.Db5, noteFunctions.D5]
DMajor5Scale = [noteFunctions.D5, noteFunctions.E5, noteFunctions.Gb5, noteFunctions.G5,
                noteFunctions.A5, noteFunctions.B5, noteFunctions.Db6, noteFunctions.D6]
DMajor6Scale = [noteFunctions.D6, noteFunctions.E6, noteFunctions.Gb6, noteFunctions.G6,
                noteFunctions.A6, noteFunctions.B6, noteFunctions.Db7, noteFunctions.D7]
DMajor7Scale = [noteFunctions.D7, noteFunctions.E7, noteFunctions.Gb7, noteFunctions.G7,
                noteFunctions.A7, noteFunctions.B7, noteFunctions.Db8, noteFunctions.D8]
DMajor8Scale = [noteFunctions.D8, noteFunctions.E8, noteFunctions.Gb8, noteFunctions.G8,
                noteFunctions.A8, noteFunctions.B8]

DMajorFullScale = DMajor1Scale + DMajor2Scale + DMajor3Scale + DMajor4Scale + DMajor5Scale + DMajor6Scale + \
                  DMajor7Scale + DMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# E Major

EMajor1Scale = [noteFunctions.E1, noteFunctions.Gb1, noteFunctions.Ab1, noteFunctions.A1,
                noteFunctions.B1, noteFunctions.Db2, noteFunctions.Eb2, noteFunctions.E2]
EMajor2Scale = [noteFunctions.E2, noteFunctions.Gb2, noteFunctions.Ab2, noteFunctions.A2,
                noteFunctions.B2, noteFunctions.Db3, noteFunctions.Eb3, noteFunctions.E3]
EMajor3Scale = [noteFunctions.E3, noteFunctions.Gb3, noteFunctions.Ab3, noteFunctions.A3,
                noteFunctions.B3, noteFunctions.Db4, noteFunctions.Eb4, noteFunctions.E4]
EMajor4Scale = [noteFunctions.E4, noteFunctions.Gb4, noteFunctions.Ab4, noteFunctions.A4,
                noteFunctions.B4, noteFunctions.Db5, noteFunctions.Eb5, noteFunctions.E5]
EMajor5Scale = [noteFunctions.E5, noteFunctions.Gb5, noteFunctions.Ab5, noteFunctions.A5,
                noteFunctions.B5, noteFunctions.Db6, noteFunctions.Eb6, noteFunctions.E6]
EMajor6Scale = [noteFunctions.E6, noteFunctions.Gb6, noteFunctions.Ab6, noteFunctions.A6,
                noteFunctions.B6, noteFunctions.Db7, noteFunctions.Eb7, noteFunctions.E7]
EMajor7Scale = [noteFunctions.E7, noteFunctions.Gb7, noteFunctions.Ab7, noteFunctions.A7,
                noteFunctions.B7, noteFunctions.Db8, noteFunctions.Eb8, noteFunctions.E8]
EMajor8Scale = [noteFunctions.E8, noteFunctions.Gb8, noteFunctions.Ab8, noteFunctions.A8,
                noteFunctions.B8]

EMajorFullScale = EMajor1Scale + EMajor2Scale + EMajor3Scale + EMajor4Scale + EMajor5Scale + EMajor6Scale + \
                  EMajor7Scale + EMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# F Major

FMajor1Scale = [noteFunctions.F1, noteFunctions.G1, noteFunctions.A1, noteFunctions.Bb1,
                noteFunctions.C2, noteFunctions.D2, noteFunctions.E2, noteFunctions.F2]
FMajor2Scale = [noteFunctions.F2, noteFunctions.G2, noteFunctions.A2, noteFunctions.Bb2,
                noteFunctions.C3, noteFunctions.D3, noteFunctions.E3, noteFunctions.F3]
FMajor3Scale = [noteFunctions.F3, noteFunctions.G3, noteFunctions.A3, noteFunctions.Bb3,
                noteFunctions.C4, noteFunctions.D4, noteFunctions.E4, noteFunctions.F4]
FMajor4Scale = [noteFunctions.F4, noteFunctions.G4, noteFunctions.A4, noteFunctions.Bb4,
                noteFunctions.C5, noteFunctions.D5, noteFunctions.E5, noteFunctions.F5]
FMajor5Scale = [noteFunctions.F5, noteFunctions.G5, noteFunctions.A5, noteFunctions.Bb5,
                noteFunctions.C6, noteFunctions.D6, noteFunctions.E6, noteFunctions.F6]
FMajor6Scale = [noteFunctions.F6, noteFunctions.G6, noteFunctions.A6, noteFunctions.Bb6,
                noteFunctions.C7, noteFunctions.D7, noteFunctions.E7, noteFunctions.F7]
FMajor7Scale = [noteFunctions.F7, noteFunctions.G7, noteFunctions.A7, noteFunctions.Bb7,
                noteFunctions.C8, noteFunctions.D8, noteFunctions.E8, noteFunctions.F8]
FMajor8Scale = [noteFunctions.F8, noteFunctions.G8, noteFunctions.A8, noteFunctions.Bb8]

FMajorFullScale = FMajor1Scale + FMajor2Scale + FMajor3Scale + FMajor4Scale + FMajor5Scale + FMajor6Scale + \
                  FMajor7Scale + FMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# G Major

GMajor1Scale = [noteFunctions.G1, noteFunctions.A1, noteFunctions.B1, noteFunctions.C2,
                noteFunctions.D2, noteFunctions.E2, noteFunctions.Gb2, noteFunctions.G2]
GMajor2Scale = [noteFunctions.G2, noteFunctions.A2, noteFunctions.B2, noteFunctions.C3,
                noteFunctions.D3, noteFunctions.E3, noteFunctions.Gb3, noteFunctions.G3]
GMajor3Scale = [noteFunctions.G3, noteFunctions.A3, noteFunctions.B3, noteFunctions.C4,
                noteFunctions.D4, noteFunctions.E4, noteFunctions.Gb4, noteFunctions.G4]
GMajor4Scale = [noteFunctions.G4, noteFunctions.A4, noteFunctions.B4, noteFunctions.C5,
                noteFunctions.D5, noteFunctions.E5, noteFunctions.Gb5, noteFunctions.G5]
GMajor5Scale = [noteFunctions.G5, noteFunctions.A5, noteFunctions.B5, noteFunctions.C6,
                noteFunctions.D6, noteFunctions.E6, noteFunctions.Gb6, noteFunctions.G6]
GMajor6Scale = [noteFunctions.G6, noteFunctions.A6, noteFunctions.B6, noteFunctions.C7,
                noteFunctions.D7, noteFunctions.E7, noteFunctions.Gb7, noteFunctions.G7]
GMajor7Scale = [noteFunctions.G7, noteFunctions.A7, noteFunctions.B7, noteFunctions.C8,
                noteFunctions.D8, noteFunctions.E8, noteFunctions.Gb8, noteFunctions.G8]
GMajor8Scale = [noteFunctions.G8, noteFunctions.A8, noteFunctions.B8]

GMajorFullScale = GMajor1Scale + GMajor2Scale + GMajor3Scale + GMajor4Scale + GMajor5Scale + GMajor6Scale + \
                  GMajor7Scale + GMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# A Major

AMajor1Scale = [noteFunctions.A1, noteFunctions.B1, noteFunctions.Db2, noteFunctions.D2,
                noteFunctions.E2, noteFunctions.Gb2, noteFunctions.Ab2, noteFunctions.A2]
AMajor2Scale = [noteFunctions.A2, noteFunctions.B2, noteFunctions.Db3, noteFunctions.D3,
                noteFunctions.E3, noteFunctions.Gb3, noteFunctions.Ab3, noteFunctions.A3]
AMajor3Scale = [noteFunctions.A3, noteFunctions.B3, noteFunctions.Db4, noteFunctions.D4,
                noteFunctions.E4, noteFunctions.Gb4, noteFunctions.Ab4, noteFunctions.A4]
AMajor4Scale = [noteFunctions.A4, noteFunctions.B4, noteFunctions.Db5, noteFunctions.D5,
                noteFunctions.E5, noteFunctions.Gb5, noteFunctions.Ab5, noteFunctions.A5]
AMajor5Scale = [noteFunctions.A5, noteFunctions.B5, noteFunctions.Db6, noteFunctions.D6,
                noteFunctions.E6, noteFunctions.Gb6, noteFunctions.Ab6, noteFunctions.A6]
AMajor6Scale = [noteFunctions.A6, noteFunctions.B6, noteFunctions.Db7, noteFunctions.D7,
                noteFunctions.E7, noteFunctions.Gb7, noteFunctions.Ab7, noteFunctions.A7]
AMajor7Scale = [noteFunctions.A7, noteFunctions.B7, noteFunctions.Db8, noteFunctions.D8,
                noteFunctions.E8, noteFunctions.Gb8, noteFunctions.Ab8, noteFunctions.A8]
AMajor8Scale = [noteFunctions.A8, noteFunctions.B8]

AMajorFullScale = AMajor1Scale + AMajor2Scale + AMajor3Scale + AMajor4Scale + AMajor5Scale + AMajor6Scale + \
                  AMajor7Scale + AMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# B Major

BMajor1Scale = [noteFunctions.B1, noteFunctions.Db2, noteFunctions.Eb2, noteFunctions.E2,
                noteFunctions.Gb2, noteFunctions.Ab2, noteFunctions.Bb2, noteFunctions.B2]
BMajor2Scale = [noteFunctions.B2, noteFunctions.Db3, noteFunctions.Eb3, noteFunctions.E3,
                noteFunctions.Gb3, noteFunctions.Ab3, noteFunctions.Bb3, noteFunctions.B3]
BMajor3Scale = [noteFunctions.B3, noteFunctions.Db4, noteFunctions.Eb4, noteFunctions.E4,
                noteFunctions.Gb4, noteFunctions.Ab4, noteFunctions.Bb4, noteFunctions.B4]
BMajor4Scale = [noteFunctions.B4, noteFunctions.Db5, noteFunctions.Eb5, noteFunctions.E5,
                noteFunctions.Gb5, noteFunctions.Ab5, noteFunctions.Bb5, noteFunctions.B5]
BMajor5Scale = [noteFunctions.B5, noteFunctions.Db6, noteFunctions.Eb6, noteFunctions.E6,
                noteFunctions.Gb6, noteFunctions.Ab6, noteFunctions.Bb6, noteFunctions.B6]
BMajor6Scale = [noteFunctions.B6, noteFunctions.Db7, noteFunctions.Eb7, noteFunctions.E7,
                noteFunctions.Gb7, noteFunctions.Ab7, noteFunctions.Bb7, noteFunctions.B7]
BMajor7Scale = [noteFunctions.B7, noteFunctions.Db8, noteFunctions.Eb8, noteFunctions.E8,
                noteFunctions.Gb8, noteFunctions.Ab8, noteFunctions.Bb8, noteFunctions.B8]
BMajor8Scale = [noteFunctions.B8]

BMajorFullScale = BMajor1Scale + BMajor2Scale + BMajor3Scale + BMajor4Scale + BMajor5Scale + BMajor6Scale + \
                  BMajor7Scale + BMajor8Scale

# ----------------------------------------------------------------------------------------------------------
# All Major Scales

allMajorScales = CMajorFullScale + DMajorFullScale + EMajorFullScale + FMajorFullScale + GMajorFullScale + \
                 AMajorFullScale + BMajorFullScale

# ----------------------------------------------------------------------------------------------------------
