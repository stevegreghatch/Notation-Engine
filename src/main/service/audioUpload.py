import librosa


def analyze_audio(file_path):
    y, sr = librosa.load(file_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    return pitches, magnitudes
