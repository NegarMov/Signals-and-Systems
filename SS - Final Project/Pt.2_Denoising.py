import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy
import scipy.io.wavfile
import scipy.signal as signal

def awgn(signal, SNR):
    # calculate the signal power and convert it to dB 
    power = np.square(signal)
    signal_avg_power = np.mean(power)
    signal_avg_db = 10 * np.log10(signal_avg_power)

    # calculate noise power
    noise_avg_db = (signal_avg_db - SNR) * 2
    noise_avg_power = 10 ** (noise_avg_db / 10)

    # generate a sample of white noise
    mean_noise = 0
    noise = np.random.normal(mean_noise, np.sqrt(noise_avg_power), len(power))

    # add the noise to the signal
    noised_signal = signal + noise

    return noised_signal

def read_audio(file):
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

        return mono, fs

def audio_to_frames(y, m, hop_size, fs):
    _, _, Zxx = signal.stft(y, fs=fs, nperseg=m, noverlap=hop_size, nfft=m * 8)
    return Zxx.T

def frames_to_audio(Y, m, hop_size, fs):
    _, xrec = signal.istft(Y.T, fs=fs, nperseg=m, noverlap=hop_size, nfft=m * 8)
    return xrec

def estimate_noise(noised_signal):
    estimated_noise = np.zeros(noised_signal.shape)
    
    # indicate the number of frames to use for estimating a-posteriori SNR
    N = 20
    
    # iterate through each frame and estimate noise
    for k in range(len(noised_signal)):
        if k < N:
            estimated_noise[k] = abs(noised_signal[k])
        else:
            a = 25        
            gamma = (abs(noised_signal[k]) ** 2) / np.mean(abs(noised_signal[k - N:k]) ** 2, axis=0) 
            alpha = 1 / (1 + np.exp(-a * (gamma - 1.5)))
            estimated_noise[k] = alpha * abs(estimated_noise[k - 1]) + (1 - alpha) * abs(noised_signal[k])
            
    return estimated_noise

def spectral_subtraction(noised_signal, noise):
    # find the magnitude and phase of the noised signal
    magnitude = abs(noised_signal)
    phase = np.angle(noised_signal)

    # subtract the noise from the magnitude of the noised signal and rebuild it by adding the original phase
    enhanced_signal = np.maximum(magnitude - noise, 0) * np.exp(1j * phase)

    return enhanced_signal

def main():
    # extract the audio signal from the file
    s, fs = read_audio('Test.wav')
    t = np.linspace(0, len(s) / fs, num=len(s))

    # add noise to the signal
    noised_signal = awgn(s, 5)

    # save the noised signal as a .wav file
    scipy.io.wavfile.write("Test_Noised.wav", fs, np.asarray(noised_signal, dtype=np.int16))

    # convert the audio signal to frames
    win_t = 30e-3
    win_f = round(fs * win_t)
    hop_size = int(win_f / 2)
    noised_signal_frames = audio_to_frames(noised_signal, win_f, hop_size, fs)
            
    # estimate the noise mean
    estimated_noise = estimate_noise(noised_signal_frames)

    # denoise the noised signal using spectral subtraction
    enhanced_signal_frames = spectral_subtraction(noised_signal_frames, estimated_noise)

    # convert the frames back to audio signal
    enhanced_signal = frames_to_audio(enhanced_signal_frames, win_f, hop_size, fs)[:len(noised_signal)]

    # save the enhanced signal as a .wav file
    scipy.io.wavfile.write("Test_Denoised.wav", fs, np.asarray(enhanced_signal, dtype=np.int16))

    # plot the original signal, the noised signal and the enhanced signal
    f, sp = plt.subplots(3)
    sp[0].plot(t, s)
    sp[0].set_title('Original Signal')
    sp[1].plot(t, noised_signal)
    sp[1].set_title('Signal with noise')
    sp[2].plot(t, enhanced_signal)
    sp[2].set_title('Enhanced signal')
    plt.show()

if __name__ == '__main__':
    main()
