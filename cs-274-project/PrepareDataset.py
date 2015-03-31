__author__ = 'varadmeru'

import warnings

warnings.filterwarnings('ignore')
import numpy as np

import featureExtractor as FE
import metaExtractor as ME
import pyaudio
import cPickle as pickle
import librosa
import wave

import sh
import converter
import scipy.io.wavfile as sciowav
import os


class PrepareDataset:
    def __init__(self, audiofile, segment_size):
        self.audiofile = audiofile
        self.hop_length = 64
        self.CHUNK = 1024
        self.sr = 44100
        self.segment_size = segment_size
        self.length = int(self.get_length(audiofile))

    # If input is not a .wav convert to .wav
    # Returns tuple of filePath to analyze and whether or not it converted
    def handleConversion(self, filePath):
        converted = False
        if os.path.splitext(filePath)[-1] != '.wav':
            filePath = converter.Convert(filePath, '.wav')
            converted = True
        return filePath, converted

    def get_length(self, filePath):
        filePath, converted = self.handleConversion(filePath)
        audio = sciowav.read(filePath)
        Fs = audio[0]
        npA = audio[1][:, 0]
        length = float(npA.shape[0]) / Fs
        if converted:
            converter.Delete(filePath)
        return length

    def delete_file(self, filePath):
        sh.rm(filePath)

    def prepare_dataset(self, audiofile):
        no_of_windows = self.length / self.segment_size

        for i in range(no_of_windows):
            y, sr = librosa.load(audiofile, duration=self.segment_size, offset=i * self.segment_size, sr=self.sr)
            stft = librosa.stft(y)
            print stft.shape
            pickle.dump(stft, open(audiofile + "-" + str(i), "wb"))

    def prepare_dataset_X_1(self, audiofile):
        no_of_windows = self.length / self.segment_size
        y, sr = librosa.load(audiofile)
        stft = librosa..stft(y)
        print stft.shape
        print stft.shape[0]
        test = stft[000:1000, :]
        print stft[400:800, :].shape[0]
        p = pyaudio.PyAudio()
        z = librosa.istft(test)
        librosa.output.write_wav("test.wav", z, sr)
        wf = wave.open("test.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(self.CHUNK)
        # play stream (3)
        while data != '':
            stream.write(data)
            data = wf.readframes(self.CHUNK)

        # # stop stream (4)
        stream.stop_stream()
        stream.close()
        self.delete_file("test.wav")

        # close PyAudio (5)
        p.terminate()


        # p = pyaudio.PyAudio()
        # print y.shape
        # for i in range(2):
        # print stft[i * self.segment_size: i * self.segment_size + self.segment_size].shape
        #
        # pickle.dump(stft, open("save.p", "wb"))
        #     test = pickle.load(open("save.p", "rb"))
        #     z = librosa.istft(test)
        #     self.delete_file("save.p")
        #     librosa.output.write_wav("test.wav", z, sr)
        #
        #     # instantiate PyAudio (1)
        #
        #     wf = wave.open("test.wav", 'rb')
        #
        #     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        #                     channels=wf.getnchannels(),
        #                     rate=wf.getframerate(),
        #                     output=True)
        #
        #     # read data
        #     data = wf.readframes(self.CHUNK)
        #
        #     # play stream (3)
        #     while data != '':
        #         stream.write(data)
        #         data = wf.readframes(self.CHUNK)
        #
        #     # # stop stream (4)
        #     stream.stop_stream()
        #     stream.close()
        #     self.delete_file("test.wav")
        #
        # # close PyAudio (5)
        # p.terminate()

    def prepare_dataset_X(self, audiofile):
        no_of_windows = self.length / self.segment_size
        y, sr = librosa.load(audiofile, sr=self.sr)
        stft = librosa.stft(y)
        p = pyaudio.PyAudio()
        # 1025, 865
        print y.shape
        for i in range(2):
            print stft[i * self.segment_size: i * self.segment_size + self.segment_size].shape

            pickle.dump(stft, open("save.p", "wb"))
            test = pickle.load(open("save.p", "rb"))
            z = librosa.istft(test)
            self.delete_file("save.p")
            librosa.output.write_wav("test.wav", z, sr)

            # instantiate PyAudio (1)

            wf = wave.open("test.wav", 'rb')

            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # read data
            data = wf.readframes(self.CHUNK)

            # play stream (3)
            while data != '':
                stream.write(data)
                data = wf.readframes(self.CHUNK)

            # # stop stream (4)
            stream.stop_stream()
            stream.close()
            self.delete_file("test.wav")

        # close PyAudio (5)
        p.terminate()


# audiofile = "GetLucky.mp3"
audiofile = "BBCSherlock-Indian.mp3"
p = PrepareDataset(audiofile, 10)
# p.prepare_dataset(audiofile)
p.prepare_dataset_X_1(audiofile)
# p.prepare_dataset_X(audiofile)

'''
def prepare_dataset(self, segment_start=0):
        print "self.length:", self.length
        print "self.segment_size:",self.segment_size
        no_of_windows = self.length / self.segment_size
        print "no_of_windows", no_of_windows
        p = pyaudio.PyAudio()

        for i in range(no_of_windows):
            y, sr = librosa.load(audiofile, duration=self.segment_size, offset=i * self.segment_size, sr=self.sr)
            stft = librosa.stft(y)

            pickle.dump(stft, open("save.p", "wb"))
            test = pickle.load(open("save.p", "rb"))
            z = librosa.istft(test)
            self.delete_file("save.p")
            librosa.output.write_wav("test.wav", z, sr)

            # instantiate PyAudio (1)

            wf = wave.open("test.wav", 'rb')

            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # read data
            data = wf.readframes(self.CHUNK)

            # play stream (3)
            while data != '':
                stream.write(data)
                data = wf.readframes(self.CHUNK)

            # # stop stream (4)
            stream.stop_stream()
            stream.close()
            self.delete_file("test.wav")

        # close PyAudio (5)
        p.terminate()
'''