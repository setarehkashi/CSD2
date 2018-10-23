import simpleaudio as sa
import time
import random 
from random import randint
import os.path 

#!/usr/bin/env python

#from midiutil import MIDIFile


#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
#track    = 0
#channel  = 0
#time     = 0    # In beats
#duration = 1    # In beats
#tempo    = 60   # In BPM
#volume   = 100  # 0-127, as per the MIDI standard

#MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
#MyMIDI.addTempo(track, time, tempo)

#for i, pitch in enumerate(degrees):
    #MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

#with open("FinalCSD.mid", "wb") as output_file:
    #MyMIDI.writeFile(output_file)
# het exporteren naar midi is niet helemaal gelukt met de code omdat er met 'time' iets mis gaat.
# ik kan niet achterhalen wat er mis gaat x



samples = [sa.WaveObject.from_wave_file("hihat.wav"),
           sa.WaveObject.from_wave_file("kick.wav"), 
           sa.WaveObject.from_wave_file("snare.wav")]

print ("what sample do you wanna play? you can choose from snare.wav or kick.wav or hihat.wav or combinations")
samplesToPlay = []

sound = input()
if (sound == "kick.wav"): 
	samplesToPlay.append(sa.WaveObject.from_wave_file("kick.wav"))
elif (sound == "snare.wav"):
 	samplesToPlay.append(sa.WaveObject.from_wave_file("snare.wav"))
elif (sound == "hihat.wav"):
 	samplesToPlay.append(sa.WaveObject.from_wave_file("hihat.wav"))
elif (sound == "combinations"):
	samplesToPlay.extend(samples)
	random.shuffle(samplesToPlay)
	
print ("good")
print ("what bpm do you wanna play with? please keep in mind you can only insert intergers as bpm values")
bpm = input()
bpm = int(bpm)
#calculate the duration of a quarternote 
quarterNoteDuration = 60 / bpm
#calculate the duration of a sixteenthNote 
sixteenthNote = quarterNoteDuration / 4.0

print ("what rhythm do you wanna play? you can choose from 5/4 or 7/8")
rhythm = input()

noteDurationsSixthEight = [ 1, 2, 4]
NoteSequence = []
for Value in NoteSequence:
	timeSequence.append(Value*sixteenthNote) #timeSequence die NoteSequence * sixteenthNote doet

timestamps = []
for timestamp in NoteSequence:
	previousValue = NoteSequence[-1]
	timestamps.append(timestamp+previousValue)

if rhythm == ("5/4"):
	while sum(NoteSequence) < 20:
		random.shuffle(noteDurationsSixthEight) # shuffle noteDurationsSixthEight
		newNote = noteDurationsSixthEight[0]   #voegt eertse element dus '1' toe en blijft doorgaan
		NoteSequence.append(newNote)
		print(NoteSequence)
		timestamps.append(newNote* quarterNoteDuration)
print (timestamps)
#print (durationSixthEight)
	
if rhythm == ("7/8"):
	while sum(NoteSequence) < 16:
		random.shuffle(noteDurationsSixthEight) # shuffle noteDurationsSixthEight
		newNote = noteDurationsSixthEight[0]   #voegt eertse element dus '1' toe en blijft doorgaan
		NoteSequence.append(newNote)
		print(NoteSequence)
		timestamps.append(newNote* quarterNoteDuration)
print (timestamps)




def playsequence (timestampssequence):
#play the sequence

	#retrive first timestamp
	timestamp = timestampssequence.pop(0)
	startTime = time.time()
	#print("startTime = " + str(startTime))
	keepPlaying = True
	while keepPlaying:
		currentTime = time.time()

		#print("currentTime - startTime = " + str(currentTime - startTime))
		#elapsedTime= currenttime - starttime
		if(currentTime - startTime >= timestamp):
			#playsample
			if len(samplesToPlay) > 0:
				randomValue = randint(0, len(samplesToPlay)-1)
			else:
				randomValue = 0
			samplesToPlay[randomValue].play()
			startTime = time.time()
			print (timestamp)
			#if there are timestamps left in the timestamplist
			if timestampssequence:

					#retrive the next timestamp 
					timestamp = timestampssequence.pop(0)
			else: 
					# list is empty, stop loop
					keepPlaying = False
		else:
			#wait for a short moemnt 
			time.sleep(0.001)

playsequence(timestamps)
