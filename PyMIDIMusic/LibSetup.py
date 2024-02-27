from ctypes import cdll
import ctypes
import os

class TPMIDIEvent(ctypes.Structure):
    _fields_ = (
        ("vptr", ctypes.c_void_p),
        ("deltaTime", ctypes.c_uint32),
    )

class TPMIDIChannelEvent(TPMIDIEvent):
    _fields_ = (
        ("vptr", ctypes.c_void_p),
        ("deltaTime", ctypes.c_uint32),
        ("channel", ctypes.c_uint32),
    )

class TNoteOn(TPMIDIChannelEvent):
    _fields_ = (
        ("vptr", ctypes.c_void_p),
        ("deltaTime", ctypes.c_uint32),
        ("channel", ctypes.c_uint32),
        ("key", ctypes.c_uint32),
        ("velocity", ctypes.c_uint32),
    )

class TNoteOff(TPMIDIChannelEvent):
    _fields_ = (
        ("vptr", ctypes.c_void_p),
        ("deltaTime", ctypes.c_uint32),
        ("channel", ctypes.c_uint32),
        ("key", ctypes.c_uint32),
    )

class TNoteOnOff(TPMIDIChannelEvent):
    _fields_ = (
        ("vptr", ctypes.c_void_p),
        ("deltaTime", ctypes.c_uint32),
        ("channel", ctypes.c_uint32),
        ("key", ctypes.c_uint32),
        ("velocity", ctypes.c_uint32),
        ("duration", ctypes.c_uint32),
    )












try:
    easyLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/EasyMidiFileParserCpp.dll')
except:
    easyLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/libEasyMidiFileParserCpp.so')
#

easyLib.MIDIEvent_GetDeltaTime.restype = ctypes.c_uint32
easyLib.MIDIEvent_GetDeltaTime.argtypes = [ctypes.c_void_p] # inherits PMIDIEvent
easyLib.MIDIEvent_SetDeltaTime.argtypes = [ctypes.c_void_p, ctypes.c_uint32] # inherits PMIDIEvent

easyLib.MIDIChannelEvent_GetChannel.restype = ctypes.c_uint32
easyLib.MIDIChannelEvent_GetChannel.argtypes = [ctypes.c_void_p] # inherits PMIDIChannelEvent
easyLib.MIDIChannelEvent_SetChannel.argtypes = [ctypes.c_void_p, ctypes.c_uint32] # inherits PMIDIChannelEvent

easyLib.NoteOn_GetKey.restype = ctypes.c_uint32
easyLib.NoteOn_GetKey.argtypes = [ctypes.c_void_p] # inherits NoteOn
easyLib.NoteOn_GetVelocity.restype = ctypes.c_uint32
easyLib.NoteOn_GetVelocity.argtypes = [ctypes.c_void_p] # inherits NoteOn

easyLib.NoteOff_GetKey.restype = ctypes.c_uint32
easyLib.NoteOff_GetKey.argtypes = [ctypes.c_void_p] # inherits NoteOff

easyLib.NoteOnOff_GetKey.restype = ctypes.c_uint32
easyLib.NoteOnOff_GetKey.argtypes = [ctypes.c_void_p] # inherits NoteOnOff
easyLib.NoteOnOff_GetVelocity.restype = ctypes.c_uint32
easyLib.NoteOnOff_GetVelocity.argtypes = [ctypes.c_void_p] # inherits NoteOnOff
easyLib.NoteOnOff_GetDuration.restype = ctypes.c_uint32
easyLib.NoteOnOff_GetDuration.argtypes = [ctypes.c_void_p] # inherits NoteOnOff

easyLib.NoteOnOff_Create.restype = ctypes.c_void_p
easyLib.NoteOn_Create.restype = ctypes.c_void_p
easyLib.NoteOff_Create.restype = ctypes.c_void_p
easyLib.PMIDIEvent_Destroy.argtypes = [ctypes.c_void_p] # inherits PMIDIEvent




class PMIDIEvent:
    isSelfAllocated = False
    internal = None # The C++ object instance
    def __init__(self, internal) -> None:
        self.internal = internal
    def __del__(self):
        if (self.isSelfAllocated):
            easyLib.PMIDIEvent_Destroy(self.internal)
    def GetDeltaTime(self):
        return easyLib.MIDIEvent_GetDeltaTime(self.internal)
    def SetDeltaTime(self, deltaTime):
        return easyLib.MIDIEvent_SetDeltaTime(self.internal, deltaTime)

class PMIDIChannelEvent(PMIDIEvent):
    def GetChannel(self):
        return easyLib.MIDIChannelEvent_GetChannel(self.internal)
    def SetChannel(self, channel):
        return easyLib.MIDIChannelEvent_SetChannel(self.internal, channel)

class NoteOn(PMIDIChannelEvent):
    def __init__(self, internal = None) -> None:
        super().__init__(internal if internal != None else easyLib.NoteOn_Create())
        self.isSelfAllocated = (internal == None)
    def GetKey(self):
        return easyLib.NoteOn_GetKey(self.internal)
    def GetVelocity(self):
        return easyLib.NoteOn_GetVelocity(self.internal)

class NoteOff(PMIDIChannelEvent):
    def __init__(self, internal = None) -> None:
        super().__init__(internal if internal != None else easyLib.NoteOff_Create())
        self.isSelfAllocated = (internal == None)
    def GetKey(self):
        return easyLib.NoteOff_GetKey(self.internal)

class NoteOnOff(PMIDIChannelEvent):
    def __init__(self, internal = None) -> None:
        super().__init__(internal if internal != None else easyLib.NoteOnOff_Create())
        self.isSelfAllocated = (internal == None)
    def GetKey(self):
        return easyLib.NoteOnOff_GetKey(self.internal)
    def GetVelocity(self):
        return easyLib.NoteOnOff_GetVelocity(self.internal)
    def GetDuration(self):
        return easyLib.NoteOnOff_GetDuration(self.internal)
    def SetKey(self, key):
        return easyLib.NoteOnOff_SetKey(self.internal, key)
    def SetVelocity(self, velocity):
        return easyLib.NoteOnOff_SetVelocity(self.internal, velocity)
    def SetDuration(self, duration):
        return easyLib.NoteOnOff_SetDuration(self.internal, duration)








class MIDIEventCallbacks(ctypes.Structure):
    _fields_ = (
        ("OnEvent", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TPMIDIEvent))), 

        ("OnSysEvent", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)),
        ("OnMetaEvent", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)), 
        ("OnChannelEvent", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TPMIDIChannelEvent))),

        ("OnNoteOn", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TNoteOn))),
        ("OnNoteOff", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TNoteOff))), 
        ("OnNoteOnOff", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(TNoteOnOff))),
        ("OnProgramChange", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)),
        ("OnControlChange", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)), 
        ("OnPitchBend", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)),
        ("OnNoteAfterTouch", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)),
        ("OnChannelAfterTouch", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)), 
    )

class TMIDIMusic(ctypes.Structure):
    _fields_ = ()


easyLib.MIDIMusic_Dispatch.argtypes = [ctypes.c_void_p, MIDIEventCallbacks, ctypes.POINTER(TMIDIMusic)]
# easyLib.MIDIMusic_Dispatch.argtypes = [MIDIEventCallbacks, ctypes.c_void_p]

# easyLib.MIDIMusic_GetDurationInTicks.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetDurationInTicks.restype = ctypes.c_uint32

easyLib.MIDIMusic_Create.restype = ctypes.POINTER(TMIDIMusic)
easyLib.MIDIMusic_Destroy.argtypes = [ctypes.POINTER(TMIDIMusic)]

easyLib.MIDIMusic_Clone.argtypes = [ctypes.POINTER(TMIDIMusic)]
easyLib.MIDIMusic_Clone.restype = ctypes.POINTER(TMIDIMusic)

easyLib.MIDIMusic_LoadFromFile.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_char_p]

easyLib.MIDIMusic_AddEvent.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_void_p] # inherits PMIDIEvent

# easyLib.MIDIMusic_GetDurationInTicks.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetDurationInTicks.restype = ctypes.c_uint32

# easyLib.MIDIMusic_GetDurationInMicroseconds.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetDurationInMicroseconds.restype = ctypes.c_double

# easyLib.MIDIMusic_GetNbChannels.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetNbChannels.restype = ctypes.c_uint32

# easyLib.MIDIMusic_GetNbTracks.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetNbTracks.restype = ctypes.c_uint32

# easyLib.MIDIMusic_GetTrack.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
# easyLib.MIDIMusic_GetTrack.restype = ctypes.c_void_p

# easyLib.MIDIMusic_GetNbEvents.argtypes = [ctypes.c_void_p]
# easyLib.MIDIMusic_GetNbEvents.restype = ctypes.c_uint32

# easyLib.MIDIMusic_GetEvent.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
# easyLib.MIDIMusic_GetEvent.restype = ctypes.c_void_p

easyLib.MIDIMusic_ConvertAbsolute.argtypes = [ctypes.POINTER(TMIDIMusic)]
easyLib.MIDIMusic_FilterChannel.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_uint8, ctypes.c_bool]
easyLib.MIDIMusic_Compress.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_int16]
easyLib.MIDIMusic_FilterInstruments.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_uint8, ctypes.c_uint8, ctypes.c_bool]
easyLib.MIDIMusic_ConvertToMonoTrack.argtypes = [ctypes.POINTER(TMIDIMusic)]
easyLib.MIDIMusic_ConvertToNoteOnOff.argtypes = [ctypes.POINTER(TMIDIMusic)]
easyLib.MIDIMusic_ConvertRelative.argtypes = [ctypes.POINTER(TMIDIMusic)]


class TTokenizer(ctypes.Structure):
    _fields_ = ()
easyLib.Tokenizer_Create.restype = ctypes.POINTER(TTokenizer)
easyLib.Tokenizer_Create.argtypes = [ctypes.POINTER(TMIDIMusic)]
easyLib.Tokenizer_Destroy.argtypes = [ctypes.POINTER(TTokenizer)]

easyLib.Tokenizer_GetNbTokens.argtypes = [ctypes.POINTER(TTokenizer)]
easyLib.Tokenizer_GetNbTokens.restype = ctypes.c_uint32

easyLib.Tokenizer_GetTokens.argtypes = [ctypes.POINTER(TTokenizer)]
easyLib.Tokenizer_GetTokens.restype = ctypes.POINTER(ctypes.c_float)

easyLib.Tokenizer_BuildTokensFromNotes1.argtypes = [ctypes.POINTER(TTokenizer)]


try:
    fluidsynthMIDIPlayerLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/FluidsynthMIDIPlayer.dll')
except:
    fluidsynthMIDIPlayerLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/libFluidsynthMIDIPlayer.so')

class TFluidsynthPlayerAsync(ctypes.Structure):
    _fields_ = ()

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Create.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_char_p]
fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Create.restype = ctypes.POINTER(TFluidsynthPlayerAsync)

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Destroy.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Play.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]
fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_PlayAsync.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]
