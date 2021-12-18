import threading
import random
import pyaudio
import numpy as np

Threshold = 10

SHORT_NORMALIZE = (1.0 / 32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2


class Controls:
    def __init__(self, p100):
        self.p100 = p100
        self.p = pyaudio.PyAudio()

        info = self.p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", self.p.get_device_info_by_host_api_device_index(0, i).get('name'))

        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=False,
                                  frames_per_buffer=chunk)

    def change_color_endless(self):
        threading.Timer(0.2, self.change_color_endless).start()
        self.p100.setColor(random.randrange(0, 360), 100, 100)

    def listen(self):
        print('Listening beginning')
        while True:
            # Read some data from input
            data = np.fromstring(self.stream.read(chunk, exception_on_overflow=False), dtype=np.int16)
            # find peaks
            peak = np.average(np.abs(data)) * 2

            # cnt = int(50 * peak / 2 ** 16)
            # if cnt < 0:
            #     cnt = 1

            print(peak)

            if peak >= 2000:
                try:
                    self.p100.setColor(random.randrange(0, 360), 100)
                except:
                    pass
