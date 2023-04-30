import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
from scipy import signal

def half_whistler_front(data, sample_rate):
    second = np.zeros(data.size)
    #second = data
    second[69000:86500] = data[0:17500]
    second[0:8750] = data[77750:86500]
    second[8750:69000] = data[8750:69000]
    second[86500:] = data[86500:]
    return second

def half_whistler_back(data, sample_rate):
    second = np.zeros(data.size)
    #second = data
    second[0:183036] = data[0:183036] 
    second[69000:86500] = data[0:17500] #deletes original whistler
    second[183036:191786] = data[69000:77750] #adds whistler to end
    return second

sample_rate, samples = wavfile.read('../data bucket/whistler/whistler0.wav')

aug_data_front = half_whistler_front(samples, sample_rate)
aug_data_back = half_whistler_back(samples, sample_rate)
# plt.plot(samples)
# plt.plot(aug_data_front)
# plt.show()

# plt.plot(samples)
# plt.plot(aug_data_back)
# plt.show()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.rcParams["figure.figsize"] = [20, 10]

frequencies_ch, times_ch, spectrogram_ch = signal.spectrogram(aug_data_front, sample_rate, noverlap=0)
frequencies_ba, times_ba, spectrogram_ba = signal.spectrogram(aug_data_back, sample_rate, noverlap=0)
    

plt.ylabel("Frequency")
plt.xlabel("Time")
plt.imshow(np.log(spectrogram_ch), origin="lower")
plt.show()

plt.ylabel("Frequency")
plt.xlabel("Time")
plt.imshow(np.log(spectrogram_ba), origin="lower")
plt.show()

    #directory --> directory of wav files
    #data_dir --> spectrogram directory