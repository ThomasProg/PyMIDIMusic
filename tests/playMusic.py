from PyMIDIMusic import *

music = MIDIMusic() 

music.LoadFromFile("C:/Users/thoma/PandorasBox/Projects/ModularMusicGenerationModules/Assets/Datasets/LakhMidi-Clean/Ludwig_van_Beethoven/Fur_Elise.1.mid")
easyLib.MIDIMusic_ConvertToMonoTrack(music.nativeObject)

music.Play("C:/Users/thoma/PandorasBox/Projects/ModularMusicGenerationModules/Assets/Soundfonts/Touhou/Touhou.sf2")
