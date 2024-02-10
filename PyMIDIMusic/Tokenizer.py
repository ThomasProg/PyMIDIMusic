from ctypes import cdll
from .LibSetup import *

class Tokenizer:
    nativeObject = None

    def __init__(self, nativeObject = None, midiMusic = None) -> None:
        self.nativeObject = nativeObject
        if (self.nativeObject == None):
            self.nativeObject = easyLib.CreateTokenizer(midiMusic)

    def __del__(self):
        easyLib.MIDIMusic_Destroy(self.nativeObject)

    def BuildTokensFromNotes1(self):
        easyLib.Tokenizer_Preprocess(self.nativeObject)
        easyLib.Tokenizer_BuildTokensFromNotes1(self.nativeObject)
        easyLib.Tokenizer_Postprocess(self.nativeObject)
    
