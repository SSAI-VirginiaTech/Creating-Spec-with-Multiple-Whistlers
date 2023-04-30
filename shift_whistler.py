import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
from scipy import signal

def time_shift(data, sample_rate, shift):
    
    shift = -shift;
    second = data
    background = second[0:17500]
    second[69000 + int(sample_rate * shift):86500 + int(sample_rate * shift)] = data[69000:86500]
    second[69000:86500] = background
    return second

sample_rate, samples = wavfile.read('../data bucket/whistler/whistler0.wav')

aug_data = time_shift(samples, sample_rate, 2.9)


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.rcParams["figure.figsize"] = [20, 10]

frequencies_ch, times_ch, spectrogram_ch = signal.spectrogram(aug_data, sample_rate, noverlap=0)
    

plt.ylabel("Frequency")
plt.xlabel("Time")
plt.imshow(np.log(spectrogram_ch), origin="lower")
plt.show()

    #directory --> directory of wav files
    #data_dir --> spectrogram directory