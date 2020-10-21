# Lumos
A python virtual assistant written solely by Astr0clad

To install:

1. Clone the repository OR download and extract the zip (from the releases)

2. Go into commands.py and change all of the filepaths that have username in them to your username

3. Run init.py using Python 3.6

(Make sure you have all the libraries installed for Python 3.6 first)

**If it does not recognize your voice, simply make a script and use this code to find your microphone index:**
```
import pyaudio
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i))
```

Then you will need to go to main.py and in line 60 change the device index to your microphone index.

If you have any issues please use the issues tab.

If you want to pull request please make a new branch with your name in it.
