from ctypes import cdll
from .LibSetup import *

class Tokenizer:
    nativeObject = None

    def __init__(self, nativeObject = None, midiMusic = None) -> None:
        self.nativeObject = nativeObject
        if (self.nativeObject == None):
            self.nativeObject = easyLib.Tokenizer_Create(midiMusic)

    def __del__(self):
        easyLib.Tokenizer_Destroy(self.nativeObject)

    def BuildTokensFromNotes1(self):
        # easyLib.Tokenizer_Preprocess(self.nativeObject)
        easyLib.Tokenizer_BuildTokensFromNotes1(self.nativeObject)
        # easyLib.Tokenizer_Postprocess(self.nativeObject)

    # def GetNbTokens(self):
    #     return easyLib.Tokenizer_GetNbTokens(self.nativeObject)

    # def GetToken(self):
    #     return easyLib.Tokenizer_GetTokens(self.nativeObject)
    
    def GetTokens(self):
        nbTokens = easyLib.Tokenizer_GetNbTokens(self.nativeObject)
        tokensPtr = easyLib.Tokenizer_GetTokens(self.nativeObject)
        floatArray = [tokensPtr[i] for i in range(nbTokens)]
        return floatArray