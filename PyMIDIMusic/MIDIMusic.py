






from ctypes import cdll
from .LibSetup import *

class MIDIMusic:
    nativeObject = None

    class Track:
        def GetNbEvents(self) -> int:
            return easyLib.MIDIMusic_GetNbEvents(self.nativeObject)
        def GetEvent(self, index: int) -> object:
            return easyLib.MIDIMusic_GetEvent(self.nativeObject, index)

    def __init__(self) -> None:

        self.nativeObject = easyLib.MIDIMusic_Create()

    def __del__(self):
        easyLib.MIDIMusic_Destroy(self.nativeObject)

    def GetDurationInTicks(self) -> int:
        return easyLib.MIDIMusic_GetDurationInTicks(self.nativeObject)
    
    def GetDurationInMicroseconds(self) -> float:
        return easyLib.MIDIMusic_GetDurationInMicroseconds(self.nativeObject)
    
    def GetNbChannels(self) -> int:
        return easyLib.MIDIMusic_GetNbChannels(self.nativeObject)
    
    def GetNbTracks(self) -> int:
        return easyLib.MIDIMusic_GetNbTracks(self.nativeObject)
    
    def GetTrack(self, index: int) -> object:
        return easyLib.MIDIMusic_GetTrack(self.nativeObject, index)
    

    
    # def GetProgramsList(self):
    #     return easyLib.MIDIMusic_GetProgramsList(self.nativeObject)

    def LoadFromFile(self, path: str):
        easyLib.MIDIMusic_LoadFromFile(self.nativeObject, path.encode('utf-8'))









