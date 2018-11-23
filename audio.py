import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 2**11
RATE = 44100
SAMPLEFREQ = 84100
FRAMESIZE = 1024

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
picos=[]
for i in range(int(10 * SAMPLEFREQ / FRAMESIZE)): # go for a few seconds
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data)) * 2
    bars = "#" * int(50 * peak / 2**16)
    print("%04d %05d %s" % (i, peak, bars))
    #plt.plot(data)
    picos.append(peak)
    if(peak>11000):
        plt.plot(data)
        print("PICOOOOOOOOOOOOOOOOOOOOOOO")

picos=np.array(picos)

print("PICO MAXIMO:",picos.max())
print("PICO MIN:",picos.min())
print("PICO AVG:",picos.mean())

plt.show()
stream.stop_stream()
stream.close()
p.terminate()
