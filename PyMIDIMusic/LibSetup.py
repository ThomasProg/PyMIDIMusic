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













easyLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/EasyMidiFileParserCpp.dll')

#

easyLib.MIDIEvent_GetDeltaTime.restype = ctypes.c_uint32
easyLib.MIDIEvent_GetDeltaTime.argtypes = [ctypes.c_void_p] # inherits PMIDIEvent

easyLib.MIDIChannelEvent_GetChannel.restype = ctypes.c_uint32
easyLib.MIDIChannelEvent_GetChannel.argtypes = [ctypes.c_void_p] # inherits PMIDIChannelEvent

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

class PMIDIEvent:
    _internal = None # The C++ object instance
    def __init__(self, internal) -> None:
        self._internal = internal
    def GetDeltaTime(self):
        return easyLib.MIDIEvent_GetDeltaTime(self._internal)

class PMIDIChannelEvent(PMIDIEvent):
    def GetChannel(self):
        return easyLib.MIDIChannelEvent_GetChannel(self._internal)

class NoteOn(PMIDIChannelEvent):
    def GetKey(self):
        return easyLib.NoteOn_GetKey(self._internal)
    def GetVelocity(self):
        return easyLib.NoteOn_GetVelocity(self._internal)

class NoteOff(PMIDIChannelEvent):
    def GetKey(self):
        return easyLib.NoteOff_GetKey(self._internal)

class NoteOnOff(PMIDIChannelEvent):
    def GetKey(self):
        return easyLib.NoteOnOff_GetKey(self._internal)
    def GetVelocity(self):
        return easyLib.NoteOnOff_GetVelocity(self._internal)
    def GetDuration(self):
        return easyLib.NoteOnOff_GetDuration(self._internal)









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


fluidsynthMIDIPlayerLib = cdll.LoadLibrary(os.path.dirname(__file__) + '/dll/FluidsynthMIDIPlayer.dll')

class TFluidsynthPlayerAsync(ctypes.Structure):
    _fields_ = ()

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Create.argtypes = [ctypes.POINTER(TMIDIMusic), ctypes.c_char_p]
fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Create.restype = ctypes.POINTER(TFluidsynthPlayerAsync)

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Destroy.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]

fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_Play.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]
fluidsynthMIDIPlayerLib.FluidsynthPlayerAsync_PlayAsync.argtypes = [ctypes.POINTER(TFluidsynthPlayerAsync)]