from .IMIDIEventReceiver import *
from .MIDIMusic import *

class Test(IMIDIEventReceiver):
    def OnEvent(self, event): pass

    def OnSysEvent(self, event): pass
    def OnMetaEvent(self, event): pass
    def OnChannelEvent(self, event): pass

    def OnNoteOn(self, event): 
        e = NoteOn(event)
        print(str(e.GetKey()))
        print(str(e.GetDeltaTime()))
    def OnNoteOff(self, event): pass
    def OnNoteOnOff(self, event): pass


music = MIDIMusic() 

music.LoadFromFile("C:/Users/thoma/PandorasBox/Projects/ModularMusicGenerationModules/Assets/Datasets/LakhMidi-Clean/Ludwig_van_Beethoven/Fur_Elise.1.mid")

Dispatch(music, Test())

