__author__ = 'varadmeru'

# We'll need the os module for file path manipulation
import os

# And numpy for some mathematical operations
import numpy as np

# Librosa for audio
import librosa

# matplotlib for displaying the output
import matplotlib.pyplot as plt

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

audiofile = "GetLucky.mp3"

y, sr = librosa.load(audiofile)

# Let's make and display a mel-scaled power (energy-squared) spectrogram
# We use a small hop length of 64 here so that the frames line up with the beat tracker example below.
S = librosa.feature.melspectrogram(y, sr=sr, n_fft=2048, hop_length=64, n_mels=3000)

# Convert to log scale (dB). We'll use the peak power as reference.
log_S = librosa.logamplitude(S, ref_power=np.max)

# Make a new figure
plt.figure(figsize=(12, 4))

# Display the spectrogram on a mel scale
# sample rate and hop length parameters are used to render the time axis
librosa.display.specshow(log_S, sr=sr, hop_length=64, x_axis='time', y_axis='mel')

# Put a descriptive title on the plot
plt.title('mel power spectrogram')

# draw a color bar
plt.colorbar(format='%+02.0f dB')

# Make the figure layout compact
plt.tight_layout()
plt.show()

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
'''
y_harmonic, y_percussive = librosa.effects.hpss(y)

# What do the spectrograms look like?
# Let's make and display a mel-scaled power (energy-squared) spectrogram
# We use a small hop length of 64 here so that the frames line up with the beat tracker example below.
S_harmonic   = librosa.feature.melspectrogram(y_harmonic, sr=sr, n_fft=2048, hop_length=64, n_mels=128)
S_percussive = librosa.feature.melspectrogram(y_percussive, sr=sr, n_fft=2048, hop_length=64, n_mels=128)

# Convert to log scale (dB). We'll use the peak power as reference.
log_Sh = librosa.logamplitude(S_harmonic, ref_power=np.max)
log_Sp = librosa.logamplitude(S_percussive, ref_power=np.max)

# Make a new figure
plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
# Display the spectrogram on a mel scale
librosa.display.specshow(log_Sh, y_axis='mel')

# Put a descriptive title on the plot
plt.title('mel power spectrogram (Harmonic)')

# draw a color bar
plt.colorbar(format='%+02.0f dB')

plt.subplot(2,1,2)
librosa.display.specshow(log_Sp, sr=sr, hop_length=64, x_axis='time', y_axis='mel')

# Put a descriptive title on the plot
plt.title('mel power spectrogram (Percussive)')

# draw a color bar
plt.colorbar(format='%+02.0f dB')

# Make the figure layout compact
plt.tight_layout()
plt.show()

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

# We'll use a longer FFT window here to better resolve low frequencies
# We'll use the harmonic component to avoid pollution from transients
C = librosa.feature.chromagram(y=y_harmonic, sr=sr, n_fft=4096, hop_length=64)

# Make a new figure
plt.figure(figsize=(12,4))

# Display the chromagram: the energy in each chromatic pitch class as a function of time
# To make sure that the colors span the full range of chroma values, set vmin and vmax
librosa.display.specshow(C, sr=sr, hop_length=64, x_axis='time', y_axis='chroma', vmin=0, vmax=1)

plt.title('Chromagram')
plt.colorbar()
plt.tight_layout()
plt.show()
'''
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################