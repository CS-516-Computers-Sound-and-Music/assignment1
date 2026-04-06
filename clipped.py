from scipy.io import wavfile as wf
import sounddevice
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Sine Wave
        Channels per frame: 1 (mono)
        Sample format: 16 bit signed (values in the range -32767..32767)
        Amplitude: ¼ maximum possible 16-bit amplitude (values in the range -8192..8192)
        Duration: one second
        Frequency: 440Hz (440 cycles per second)
        Sample Rate: 48000 samples per second
    """
    amplitude = 8192
    frequency = 400
    sample_rate = 48000

    sin_x = np.linspace(0,1,sample_rate)
    sin_y = amplitude * np.sin(2*np.pi*frequency*sin_x)

    # save to sine.wav
    
    wf.write("sine.wav", sample_rate, sin_y)

    # note: worst sound I've ever heard, so loud
    """
    Fixing loudness on replay: dividing the entire thing by a constant (large to make it a lot less loud)
    The raw sound was blowing out my speakers, so it didn't even sound like middle A (much higher than)
    The volumne control of 100 000 sounds like A and doesn't hurt

    So, what I've found is that, even through quicktime, the amplitude bypasses my computer's volume 
    controls.
    """
    vol_control = 10000 # much better
    sounddevice.play(sin_y/vol_control, samplerate=sample_rate)
    sounddevice.wait()
    
    """Clipped Sine Wave
    half amplitude wave clipped at +/- 8192
    """
    max_amp = 8192

    clipped_y = sin_y*2
    clipped_y[clipped_y>max_amp] = max_amp
    clipped_y[clipped_y<-max_amp] = -max_amp

    # write to clipped.wav
    wf.write("clipped.wav", sample_rate, clipped_y)

    # play it back
    sounddevice.play(clipped_y/vol_control, samplerate=sample_rate)
    sounddevice.wait()


    # Show the two waves
    stop = 200
    plt.plot(sin_x[:stop], sin_y[:stop], label="Sine Wave")
    plt.plot(sin_x[:stop], sin_y[:stop]*2, c='orange',linestyle='dashed')
    plt.plot(sin_x[:stop], clipped_y[:stop], c="orange", label="Clipped Sine Wave")

    plt.title(f"{frequency}Hz Sine Waves")
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()