from ctypes import cdll
import ctypes
from .MIDIMusic import *
from .LibSetup import *

class IMIDIEventReceiver:
    def OnEvent(self, event): pass

    def OnSysEvent(self, event): pass
    def OnMetaEvent(self, event): pass
    def OnChannelEvent(self, event): pass

    def OnNoteOn(self, event): pass
    def OnNoteOff(self, event): pass
    def OnNoteOnOff(self, event): pass

    def OnTimeSignature(self, event): pass
    
def Dispatch(music: MIDIMusic, eventReceiver: IMIDIEventReceiver):
    callbacks = MIDIEventCallbacks()

    def LocalOnEvent(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnEvent(event)
    callbacks.OnEvent = type(callbacks.OnEvent)(LocalOnEvent)
    
    def LocalOnSysEvent(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnSysEvent(event)
    callbacks.OnSysEvent = type(callbacks.OnSysEvent)(LocalOnSysEvent)
    
    def LocalOnMetaEvent(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnMetaEvent(event)
    callbacks.OnMetaEvent = type(callbacks.OnMetaEvent)(LocalOnMetaEvent)
    
    def LocalOnChannelEvent(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnChannelEvent(event)
    callbacks.OnChannelEvent = type(callbacks.OnChannelEvent)(LocalOnChannelEvent)

    def LocalOnNoteOn(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnNoteOn(event)
    callbacks.OnNoteOn = type(callbacks.OnNoteOn)(LocalOnNoteOn)

    def LocalOnNoteOnOff(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnNoteOnOff(event)
    callbacks.OnNoteOnOff = type(callbacks.OnNoteOnOff)(LocalOnNoteOnOff)

    def LocalOnNoteOff(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnNoteOff(event)
    callbacks.OnNoteOff = type(callbacks.OnNoteOff)(LocalOnNoteOff)

    def LocalOnTimeSignature(a, event):
        originalInstance = ctypes.cast(a, ctypes.POINTER(ctypes.py_object)).contents.value
        originalInstance.OnTimeSignature(event)
    callbacks.OnTimeSignature = type(callbacks.OnTimeSignature)(LocalOnTimeSignature)

    # @TODO : Other callbacks

    my_instance_ptr = ctypes.cast(ctypes.pointer(ctypes.py_object(eventReceiver)), ctypes.c_void_p)
    
    easyLib.MIDIMusic_Dispatch(my_instance_ptr, callbacks, music.nativeObject) 


