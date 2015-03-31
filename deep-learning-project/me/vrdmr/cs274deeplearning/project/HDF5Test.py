import h5py

def __main__():
    h5 = hdf5_getters.open_h5_file_read("")
    duration = hdf5_getters.get_duration(h5)
    h5.close()
