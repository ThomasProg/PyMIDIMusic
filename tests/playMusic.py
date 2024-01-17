from PyMIDIMusic import *

music = MIDIMusic() 

midiFile = input("Enter a midi file path : ")
music.LoadFromFile(midiFile)
easyLib.MIDIMusic_ConvertToMonoTrack(music.nativeObject)

sfFile = input("Enter a soundfont file path : ")
music.Play(sfFile)

while(True):
    s = input()
    if (s == "stop"):
        break
