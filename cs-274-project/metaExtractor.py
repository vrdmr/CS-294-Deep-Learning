import eyed3
from pprint import pprint
import os
import converter
import scipy.io.wavfile as sciowav


class Meta(object):
    def __init__(self, mp3Data, filepath=""):
        self.artist = mp3Data.tag.artist
        self.album = mp3Data.tag.album
        self.title = mp3Data.tag.title
        self.track_num = mp3Data.tag.track_num
        self.genre = mp3Data.tag.genre.name
        self.date = mp3Data.tag.best_release_date.year

    def __str__(self):
        return str(self.__dict__)

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


# Extracting mp3 id3 tag data
def metaData(filePath):
    try:
        mp3Data = eyed3.load(filePath)
        metaData = Meta(mp3Data, filePath)
        return metaData
    except:
        print 'no metaData detected'
        return None