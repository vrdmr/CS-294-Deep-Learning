__author__ = 'varadmeru'

# We'll need the os module for file path manipulation

# And numpy for some mathematical operations
import numpy as np

import featureExtractor as FE
import metaExtractor as ME
import pyaudio
import cPickle as pickle
import librosa
import wave
import warnings

hop_length = 64
CHUNK = 1024
sr=44100

filePath = "GetLucky.mp3"
print(filePath)

warnings.warn("deprecated", DeprecationWarning)
f = open("temp.txt", mode="w")

y, sr = librosa.load(filePath, duration=10, offset=10, sr=sr)
stft = librosa.stft(y)

print stft[0, :]
print stft.ndim
print stft.size
print stft.shape
print stft.tolist().__sizeof__()
pickle.dump(stft, open("save.p", "wb"))
test = pickle.load(open("save.p", "rb"))
z = librosa.istft(test)
librosa.output.write_wav("test_wav.wav", z, sr)

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

wf = wave.open("test_wav.wav", 'rb')

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)
#
# # play stream (3)
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

# # stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()

"""
GetLucky.mp3
[[ -2.06915885e-02 -0.00000000e+00j  -2.07008086e-02 -0.00000000e+00j
   -2.07013283e-02 -0.00000000e+00j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  1.02376919e-02 +5.45150405e-18j   1.04440022e-02 +5.59795262e-06j
    1.03067756e-02 -6.39934933e-06j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  1.49401531e-04 -2.61459093e-20j  -2.19004374e-04 -5.17934750e-05j
    2.41193819e-04 -1.32401212e-04j ...,   0.00000000e+00 +0.00000000e+00j
    0.00000000e+00 +0.00000000e+00j   0.00000000e+00 +0.00000000e+00j]
 ...,
 [  2.07551675e-05 +5.07098648e-20j  -1.03765024e-05 -4.70088812e-09j
   -4.63836969e-09 +3.88920718e-09j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [ -2.07523499e-05 +1.69406589e-20j  -1.61951974e-09 -1.03755729e-05j
   -2.49379906e-10 -2.30542563e-09j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  2.07532121e-05 -0.00000000e+00j   1.03773200e-05 -0.00000000e+00j
   -1.31596489e-09 -0.00000000e+00j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]]
10966475
(1025, 10699)
8240
[[ -2.06915885e-02 -0.00000000e+00j  -2.07008086e-02 -0.00000000e+00j
   -2.07013283e-02 -0.00000000e+00j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  1.02376919e-02 +5.45150405e-18j   1.04440022e-02 +5.59795262e-06j
    1.03067756e-02 -6.39934933e-06j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  1.49401531e-04 -2.61459093e-20j  -2.19004374e-04 -5.17934750e-05j
    2.41193819e-04 -1.32401212e-04j ...,   0.00000000e+00 +0.00000000e+00j
    0.00000000e+00 +0.00000000e+00j   0.00000000e+00 +0.00000000e+00j]
 ...,
 [  2.07551675e-05 +5.07098648e-20j  -1.03765024e-05 -4.70088812e-09j
   -4.63836969e-09 +3.88920718e-09j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [ -2.07523499e-05 +1.69406589e-20j  -1.61951974e-09 -1.03755729e-05j
   -2.49379906e-10 -2.30542563e-09j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]
 [  2.07532121e-05 -0.00000000e+00j   1.03773200e-05 -0.00000000e+00j
   -1.31596489e-09 -0.00000000e+00j ...,   0.00000000e+00 -0.00000000e+00j
    0.00000000e+00 -0.00000000e+00j   0.00000000e+00 -0.00000000e+00j]]
"""
#
# segments = FE.segmentData(filePath)
# meta = ME.metaData(filePath)
#
# print "meta", meta
# segment = segments[0]
# print "FE.FFTSegment(segment)", FE.FFTSegment(segment,)
# print "segment.__sizeof__", segment.__sizeof__()
# print "len(segment)"
# print "len(segments)", len(segments)
# print "segment.start", segment.start
# print "segment.end", segment.end
# print "segment.duration", segment.duration
# print "segment.loudness", segment.loudness
# print "segment.pitches", segment.pitches
# print "segment.timbre", segment.timbre


# y, sr = librosa.load(audiofile)

# Let's make and display a mel-scaled power (energy-squared) spectrogram
# We use a small hop length of 64 here so that the frames line up with the beat tracker example below.
# S = librosa.feature.melspectrogram(y, sr=sr, n_fft=2048, hop_length=64, n_mels=128)
# print S.size
# print S.shape
# print S[1:2, :]
# print S[1:2, :].ndim
# print S[1:2, :].shape
# S[1:2, :].tofile('try.txt', ",")

# Convert to log scale (dB). We'll use the peak power as reference.
# log_S = librosa.logamplitude(S, ref_power=np.max)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

# y_harmonic, y_percussive = librosa.effects.hpss(y)
# librosa.output.write_wav('y_harmonic', y_harmonic, sr)
# librosa.output.write_wav('y_percussive', y_percussive, sr)

# What do the spectrograms look like?
# Let's make and display a mel-scaled power (energy-squared) spectrogram
# We use a small hop length of 64 here so that the frames line up with the beat tracker example below.
# S_harmonic = librosa.feature.melspectrogram(y_harmonic, sr=sr, n_fft=2048, hop_length=64, n_mels=128)
# S_percussive = librosa.feature.melspectrogram(y_percussive, sr=sr, n_fft=2048, hop_length=64, n_mels=128)
# # Convert to log scale (dB). We'll use the peak power as reference.
# log_Sh = librosa.logamplitude(S_harmonic, ref_power=np.max)
# log_Sp = librosa.logamplitude(S_percussive, ref_power=np.max)

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
# Next, we'll extract the top 20 Mel-frequency cepstral coefficients (MFCCs)
# mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=12)
# delta_mfcc = librosa.feature.delta(mfcc)
# delta2_mfcc = librosa.feature.delta(mfcc, order=2)
#
# # For future use, we'll stack these together into one matrix
# M = np.vstack([mfcc, delta_mfcc, delta2_mfcc])

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

# We'll use a longer FFT window here to better resolve low frequencies
# We'll use the harmonic component to avoid pollution from transients
# C = librosa.feature.chromagram(y=y_harmonic, sr=sr, n_fft=4096, hop_length=64)
# librosa.output.write_wav('chromagram', C, sr)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

# tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=sr, hop_length=64)
# beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=hop_length)
# librosa.output.frames_csv(os.path.join(os.curdir, 'beats.csv'), beat_times)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
