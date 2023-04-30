import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
from scipy import signal

def add_whistler(data, sample_rate, shift, direction):
    
    if direction == 'left':
        shift = -shift;
    second = np.zeros(data.size)
    second[69000 + int(sample_rate * shift):86500 + int(sample_rate * shift)] = data[69000:86500]
    return second

sample_rate, samples = wavfile.read('../data bucket/whistler/whistler0.wav')

aug_data = add_whistler(samples, sample_rate, 0.1, 'left')
# plt.plot(samples)
# plt.plot(aug_data)
# plt.show()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.rcParams["figure.figsize"] = [20, 10]

frequencies_or, times_or, spectrogram_or = signal.spectrogram(aug_data + samples, sample_rate, noverlap=0)
# frequencies_ch, times_ch, spectrogram_ch = signal.spectrogram(aug_data, sample_rate)

# for j in range(spectrogram_or.shape[1]):
#     mean = 0.0
#     for i in range(spectrogram_or.shape[0]):
#         mean += spectrogram_or[i, j]
#     mean = mean / 129
#     for i in range(spectrogram_or.shape[0]):
#         spectrogram_or[i, j] = max(spectrogram_or[i, j] - mean, 0.0)
        
plt.imshow(np.log(spectrogram_or), origin="lower")
plt.show()
    #directory --> directory of wav files
    #data_dir --> spectrogram directory