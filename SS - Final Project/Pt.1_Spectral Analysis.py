import matplotlib.pyplot as plt
import numpy as np
import wave
import os
import re

def find_max_freq(file):
    with wave.open(file, 'r') as wav_file:
        # read the .wav file
        signal = wav_file.readframes(-1)
        signal = np.frombuffer(signal, 'int16')

        # in case the audio is stereo, only pick the first channel
        channels = [[] for _ in range(wav_file.getnchannels())]
        for index, datum in enumerate(signal):
            channels[index % len(channels)].append(datum)
        mono = channels[0]

        # find the frame rate of the audio
        fs = wav_file.getframerate()

        # calculate the power spectrum of the audio signal
        power_spectrum = np.square(np.abs(np.fft.rfft(mono)))
        freqs = np.fft.rfftfreq(len(mono), 1 / fs)
        idx = np.argsort(freqs)

        # find the frequency at which the power spectrum reaches its maximum value
        max_frequency = freqs[idx][np.argmax(power_spectrum[idx])]

        """ PLOT THE POWER SPECTRUM
        max_point = (max_frequency, np.max(power_spectrum))

        plt.title(f"Power Spectrum Graph of {file}", color='royalblue')
        plt.plot(freqs[idx], power_spectrum[idx])
        plt.annotate(f"Max at frequency: {round(max_frequency, 3)} Hz", max_point, color='indigo')
        plt.xlabel('Frequency')
        plt.ylabel('Power')
        plt.show()
        """

        return max_frequency

def label_voices(path):
    labels = []

    # iterate over all the files in the given path and label them
    files = os.listdir(path)
    files.sort(key=lambda f: int(re.sub('\D', '', f)))
    for file in files:
        max_frequency = find_max_freq(f"{path}/{file}")
        labels.append('Male' if max_frequency < 170 else 'Female')
    return labels

def main():
    labels = label_voices('./voices')
    print(labels)

if __name__ == '__main__':
    main()