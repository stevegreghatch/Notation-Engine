import winsound
import noteDuration
import random
import noteScale

def playRandomFromSelection(selection):
    playback = []
    for i in range(50):
        playback.append(random.choice(selection))
    # print(playback)
    for note in playback:
        note()
        print(note.__name__)

def playRandomStructuredByScale(selection):
    # selects next note by using same key of previously played note
    playback = []

    # first note
    firstNoteToAdd = random.choice(selection)
    playback.append(firstNoteToAdd)
    print("First Note:", firstNoteToAdd.__name__)

    # keep track of last played note
    previousNoteAdded = playback[-1]

    # select next note in same key
    for i in range(49):
        listOfAllNotesInSameScales = checkScale(previousNoteAdded)
        listOfNotesInRandomScale = random.choice(listOfAllNotesInSameScales)
        nextNoteToAdd = random.choice(listOfNotesInRandomScale)
        playback.append(nextNoteToAdd)
        print("Next Note: ", nextNoteToAdd.__name__)
    # print("All Notes:", playback)

    for note in playback:
        note()

def getListOfNotesInScales():
    # get list of notes in scale
    for note in noteScale.CMajorFullScale:
        noteScale.listOfNoteNamesInCMajorScale.append(note.__name__)
    for note in noteScale.DMajorFullScale:
        noteScale.listOfNoteNamesInDMajorScale.append(note.__name__)
    for note in noteScale.EMajorFullScale:
        noteScale.listOfNoteNamesInEMajorScale.append(note.__name__)
    for note in noteScale.FMajorFullScale:
        noteScale.listOfNoteNamesInFMajorScale.append(note.__name__)
    for note in noteScale.GMajorFullScale:
        noteScale.listOfNoteNamesInGMajorScale.append(note.__name__)
    for note in noteScale.AMajorFullScale:
        noteScale.listOfNoteNamesInAMajorScale.append(note.__name__)
    for note in noteScale.BMajorFullScale:
        noteScale.listOfNoteNamesInBMajorScale.append(note.__name__)

def checkScale(noteFrequency):

    # get name of note to check
    noteNameToCheck = noteFrequency.__name__

    listOfAllNotesInSameScales = []
    getListOfNotesInScales()

    # search list for note to check
    if noteNameToCheck in noteScale.listOfNoteNamesInCMajorScale:
        print("note is in C Major scale")
        listOfAllNotesInSameScales.append(noteScale.CMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInDMajorScale:
        print("note is in D Major scale")
        listOfAllNotesInSameScales.append(noteScale.DMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInEMajorScale:
        print("note is in E Major scale")
        listOfAllNotesInSameScales.append(noteScale.EMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInFMajorScale:
        print("note is in F Major scale")
        listOfAllNotesInSameScales.append(noteScale.FMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInGMajorScale:
        print("note is in G Major scale")
        listOfAllNotesInSameScales.append(noteScale.GMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInAMajorScale:
        print("note is in A Major scale")
        listOfAllNotesInSameScales.append(noteScale.AMajorFullScale)
    if noteNameToCheck in noteScale.listOfNoteNamesInBMajorScale:
        print("note is in B Major scale")
        listOfAllNotesInSameScales.append(noteScale.BMajorFullScale)

    # return list of notes in scale
    # print(listOfAllNotesInSameScales)
    return listOfAllNotesInSameScales

# ascending and descending scale
def playScale(selection):

    playbackAscendingScale = []
    playbackDescendingScale = []

    for note in selection:
        playbackAscendingScale.append(note)
    for note in reversed(selection):
        playbackDescendingScale.append(note)

    for note in playbackAscendingScale:
        note()
    for note in playbackDescendingScale:
        note()


#  notes ---------------------------------------------------------------------------
def D1():
    winsound.Beep(37, noteDuration.duration('quarter'))
def Eb1():
    winsound.Beep(39, noteDuration.duration('quarter'))
def E1():
    winsound.Beep(41, noteDuration.duration('quarter'))
def F1():
    winsound.Beep(44, noteDuration.duration('quarter'))
def Gb1():
    winsound.Beep(46, noteDuration.duration('quarter'))
def G1():
    winsound.Beep(49, noteDuration.duration('quarter'))
def Ab1():
    winsound.Beep(52, noteDuration.duration('quarter'))
def A1():
    winsound.Beep(55, noteDuration.duration('quarter'))
def Bb1():
    winsound.Beep(58, noteDuration.duration('quarter'))
def B1():
    winsound.Beep(62, noteDuration.duration('quarter'))
#
def C2():
    winsound.Beep(65, noteDuration.duration('quarter'))
def Db2():
    winsound.Beep(69, noteDuration.duration('quarter'))
def D2():
    winsound.Beep(73, noteDuration.duration('quarter'))
def Eb2():
    winsound.Beep(78, noteDuration.duration('quarter'))
def E2():
    winsound.Beep(82, noteDuration.duration('quarter'))
def F2():
    winsound.Beep(87, noteDuration.duration('quarter'))
def Gb2():
    winsound.Beep(93, noteDuration.duration('quarter'))
def G2():
    winsound.Beep(98, noteDuration.duration('quarter'))
def Ab2():
    winsound.Beep(104, noteDuration.duration('quarter'))
def A2():
    winsound.Beep(110, noteDuration.duration('quarter'))
def Bb2():
    winsound.Beep(117, noteDuration.duration('quarter'))
def B2():
    winsound.Beep(123, noteDuration.duration('quarter'))
#
def C3():
    winsound.Beep(131, noteDuration.duration('quarter'))
def Db3():
    winsound.Beep(139, noteDuration.duration('quarter'))
def D3():
    winsound.Beep(147, noteDuration.duration('quarter'))
def Eb3():
    winsound.Beep(156, noteDuration.duration('quarter'))
def E3():
    winsound.Beep(165, noteDuration.duration('quarter'))
def F3():
    winsound.Beep(175, noteDuration.duration('quarter'))
def Gb3():
    winsound.Beep(185, noteDuration.duration('quarter'))
def G3():
    winsound.Beep(196, noteDuration.duration('quarter'))
def Ab3():
    winsound.Beep(208, noteDuration.duration('quarter'))
def A3():
    winsound.Beep(220, noteDuration.duration('quarter'))
def Bb3():
    winsound.Beep(223, noteDuration.duration('quarter'))
def B3():
    winsound.Beep(247, noteDuration.duration('quarter'))
#
def C4():
    winsound.Beep(262, noteDuration.duration('quarter'))
def Db4():
    winsound.Beep(277, noteDuration.duration('quarter'))
def D4():
    winsound.Beep(294, noteDuration.duration('quarter'))
def Eb4():
    winsound.Beep(311, noteDuration.duration('quarter'))
def E4():
    winsound.Beep(330, noteDuration.duration('quarter'))
def F4():
    winsound.Beep(349, noteDuration.duration('quarter'))
def Gb4():
    winsound.Beep(370, noteDuration.duration('quarter'))
def G4():
    winsound.Beep(392, noteDuration.duration('quarter'))
def Ab4():
    winsound.Beep(415, noteDuration.duration('quarter'))
def A4():
    winsound.Beep(440, noteDuration.duration('quarter'))
def Bb4():
    winsound.Beep(466, noteDuration.duration('quarter'))
def B4():
    winsound.Beep(494, noteDuration.duration('quarter'))
#
def C5():
    winsound.Beep(523, noteDuration.duration('quarter'))
def Db5():
    winsound.Beep(554, noteDuration.duration('quarter'))
def D5():
    winsound.Beep(587, noteDuration.duration('quarter'))
def Eb5():
    winsound.Beep(622, noteDuration.duration('quarter'))
def E5():
    winsound.Beep(659, noteDuration.duration('quarter'))
def F5():
    winsound.Beep(698, noteDuration.duration('quarter'))
def Gb5():
    winsound.Beep(740, noteDuration.duration('quarter'))
def G5():
    winsound.Beep(784, noteDuration.duration('quarter'))
def Ab5():
    winsound.Beep(831, noteDuration.duration('quarter'))
def A5():
    winsound.Beep(880, noteDuration.duration('quarter'))
def Bb5():
    winsound.Beep(932, noteDuration.duration('quarter'))
def B5():
    winsound.Beep(988, noteDuration.duration('quarter'))
#
def C6():
    winsound.Beep(1047, noteDuration.duration('quarter'))
def Db6():
    winsound.Beep(1109, noteDuration.duration('quarter'))
def D6():
    winsound.Beep(1175, noteDuration.duration('quarter'))
def Eb6():
    winsound.Beep(1245, noteDuration.duration('quarter'))
def E6():
    winsound.Beep(1319, noteDuration.duration('quarter'))
def F6():
    winsound.Beep(1397, noteDuration.duration('quarter'))
def Gb6():
    winsound.Beep(1480, noteDuration.duration('quarter'))
def G6():
    winsound.Beep(1568, noteDuration.duration('quarter'))
def Ab6():
    winsound.Beep(1661, noteDuration.duration('quarter'))
def A6():
    winsound.Beep(1760, noteDuration.duration('quarter'))
def Bb6():
    winsound.Beep(1865, noteDuration.duration('quarter'))
def B6():
    winsound.Beep(1976, noteDuration.duration('quarter'))
#
def C7():
    winsound.Beep(2093, noteDuration.duration('quarter'))
def Db7():
    winsound.Beep(2217, noteDuration.duration('quarter'))
def D7():
    winsound.Beep(2349, noteDuration.duration('quarter'))
def Eb7():
    winsound.Beep(2489, noteDuration.duration('quarter'))
def E7():
    winsound.Beep(2637, noteDuration.duration('quarter'))
def F7():
    winsound.Beep(2794, noteDuration.duration('quarter'))
def Gb7():
    winsound.Beep(2960, noteDuration.duration('quarter'))
def G7():
    winsound.Beep(3136, noteDuration.duration('quarter'))
def Ab7():
    winsound.Beep(3322, noteDuration.duration('quarter'))
def A7():
    winsound.Beep(3520, noteDuration.duration('quarter'))
def Bb7():
    winsound.Beep(3729, noteDuration.duration('quarter'))
def B7():
    winsound.Beep(3951, noteDuration.duration('quarter'))
#
def C8():
    winsound.Beep(4186, noteDuration.duration('quarter'))
def Db8():
    winsound.Beep(4435, noteDuration.duration('quarter'))
def D8():
    winsound.Beep(4699, noteDuration.duration('quarter'))
def Eb8():
    winsound.Beep(4978, noteDuration.duration('quarter'))
def E8():
    winsound.Beep(5274, noteDuration.duration('quarter'))
def F8():
    winsound.Beep(5588, noteDuration.duration('quarter'))
def Gb8():
    winsound.Beep(5920, noteDuration.duration('quarter'))
def G8():
    winsound.Beep(6272, noteDuration.duration('quarter'))
def Ab8():
    winsound.Beep(6645, noteDuration.duration('quarter'))
def A8():
    winsound.Beep(7040, noteDuration.duration('quarter'))
def Bb8():
    winsound.Beep(7459, noteDuration.duration('quarter'))
def B8():
    winsound.Beep(7902, noteDuration.duration('quarter'))
