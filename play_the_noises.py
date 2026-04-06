from scipy.io import wavfile as wf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

vol = lambda x:x/10000

def main():
    sample_rate, ac_data = wf.read("asymm_clipped.wav")
    _, clip_data = wf.read("clipped.wav")
    _, s_data = wf.read("sine.wav")

    sd.play(vol(s_data), samplerate=sample_rate)
    sd.wait()

    sd.play(vol(clip_data), samplerate=sample_rate)
    sd.wait()

    sd.play(vol(ac_data), samplerate=sample_rate)
    sd.wait()
    
if __name__ == "__main__":
    main()