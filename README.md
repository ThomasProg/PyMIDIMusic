

Uses [Hatch](https://pypi.org/project/hatch/) as a build backend by default.

To install build tools:
```
py -m pip install --upgrade build
```

To build:
```
py -m build
```

# Locally

```
pip install ./
```

To know where it is installed, you can also use:
```
python -m pip install . --verbose
```

# Online

To upload the package, install Twine: 
```
py -m pip install --upgrade twine
```

To upload the package:
```
py -m twine upload --repository testpypi dist/*
```

```
  username = __token__
  password = pypi-[THE TOKEN YOU GOT FROM test.pypi.org/]
```

To install the package from the test repository:
```
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps PyEasyMidiFileParserCpp
```

To use the package in your code:
```py
from PyEasyMidiFileParserCpp import *
```

To install locally:
```
pip install -e ./
```

On linux, if you get this error message when importing the library: `version GLIBCXX_3.4.32' not found`
then make sure to install libstdcxx-ng: `conda install -c conda-forge libstdcxx-ng`

# Usage

Display notes per channel:
```py
from PyMIDIMusic import *
import matplotlib.pyplot as plt

class Test(IMIDIEventReceiver):
    channels = []
    times = []
    notes = []
    colors = []

    def OnEvent(self, event): pass

    def OnSysEvent(self, event): pass
    def OnMetaEvent(self, event): pass
    def OnChannelEvent(self, event): pass

    def OnNoteOn(self, event): 
        e = NoteOn(event)
        self.times.append(e.GetDeltaTime())
        self.notes.append(e.GetKey())
        self.channels.append(e.GetChannel())
    def OnNoteOff(self, event): pass
    def OnNoteOnOff(self, event): pass


music = MIDIMusic() 

music.LoadFromFile("C:/Users/thoma/PandorasBox/Projects/ModularMusicGenerationModules/Assets/Datasets/LakhMidi-Clean/Ludwig_van_Beethoven/Fur_Elise.1.mid")

# easyLib.MIDIMusic_FilterChannel(music.nativeObject, 9, True)
# easyLib.MIDIMusic_FilterInstruments(music.nativeObject, 0, 7, False)

easyLib.MIDIMusic_ConvertAbsolute(music.nativeObject)

test = Test()
Dispatch(music, test)

plt.figure(figsize=(10, 5))
plt.scatter(test.times, test.channels, marker='o')

plt.xlabel('Time')
plt.ylabel('Channel')
plt.title("Notes per channel")

plt.show()
```

