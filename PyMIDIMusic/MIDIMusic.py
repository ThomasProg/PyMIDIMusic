






from ctypes import cdll
from .LibSetup import *

class MIDIMusic:
    nativeObject = None
    _player = None

    class Track:
        def GetNbEvents(self) -> int:
            return easyLib.MIDIMusic_GetNbEvents(self.nativeObject)
        def GetEvent(self, index: int) -> object:
            return easyLib.MIDIMusic_GetEvent(self.nativeObject, index)

    def __init__(self, nativeObject = None) -> None:
        self.nativeObject = nativeObject
        if (self.nativeObject == None):
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
    
    def Play(self, soundfontPath: str):
        if (self._player != None):
            self.Stop()
        self._player = fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Create(self.nativeObject, soundfontPath.encode('utf-8'))
        fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_PlayAsync(self._player)

    def Stop(self):
        fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Destroy(self._player)
        self._player = None
    
    # def GetProgramsList(self):
    #     return easyLib.MIDIMusic_GetProgramsList(self.nativeObject)

    def LoadFromFile(self, path: str):
        easyLib.MIDIMusic_LoadFromFile(self.nativeObject, path.encode('utf-8'))

    def Clone(self):
        newMusicNativeObject = easyLib.MIDIMusic_Clone(self.nativeObject)
        return MIDIMusic(nativeObject=newMusicNativeObject)

    def AddEvent(self, event: PMIDIEvent):
        easyLib.MIDIMusic_AddEvent(self.nativeObject, event.internal)
        event.isSelfAllocated = False







