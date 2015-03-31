__author__ = 'varadmeru'

import os
import sys
import time
import glob
import datetime
import sqlite3
import numpy as np


msd_subset_path = '/Users/varadmeru/uci-related/uci-courses/cs274c-deeplearning/MillionSongSubset'
msd_subset_data_path = os.path.join(msd_subset_path, 'data')
msd_subset_addf_path = os.path.join(msd_subset_path, 'Additional Files')
assert os.path.isdir(msd_subset_path), 'wrong path'

msd_code_path = '/Users/varadmeru/uci-related/uci-courses/cs274c-deeplearning/MSongsDB'
assert os.path.isdir(msd_code_path), 'wrong path'
sys.path.append(os.path.join(msd_code_path, 'PythonSrc'))

import hdf5_getters as GETTERS


def strtimedelta(starttime, stoptime):
    return str(datetime.timedelta(seconds=stoptime - starttime))


def apply_to_all_files(basedir, func=lambda x: x, ext='.h5'):
    cnt = 0
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, '*' + ext))
        cnt += len(files)
        for f in files:
            func(f)
    return cnt


print 'number of song files :', apply_to_all_files(msd_subset_data_path)
'''
number of song files : 10000
'''

all_artist_names = set()
def func_to_get_artist_name(filename):
    h5 = GETTERS.open_h5_file_read(filename)
    artist_name = GETTERS.get_artist_name(h5)
    all_artist_names.add(artist_name)
    h5.close()


t1 = time.time()
apply_to_all_files(msd_subset_data_path, func=func_to_get_artist_name)
t2 = time.time()

print 'all artist names extracted in: ', strtimedelta(t1, t2)
print 'found', len(all_artist_names), 'unique artist names'

for k in range(5):
    print list(all_artist_names)[k]

conn = sqlite3.connect(os.path.join(msd_subset_addf_path, 'subset_track_metadata.db'))
q = 'SELECT DISTINCT artist_name FROM songs'

t1 = time.time()
res = conn.execute(q)
all_artist_names_sqlite = res.fetchall()
t2 = time.time()
conn.close()

print 'all artist names extracted (SQLite) in: ', strtimedelta(t1, t2)

for k in range(5):
    print all_artist_names_sqlite[k][0]