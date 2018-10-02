import simpleaudio as sa 
import time
import random



samples = [sa.WaveObject.from_wave_file("snare.wav"),
           sa.WaveObject.from_wave_file("kick2.wav")]


bpm = 120
#calculate the duration of a quarternote
quarterNoteDuration = 60 / bpm
#calculate the duration of a SixteenthNote
sixteenthNoteDuration = quarterNoteDuration / 4.0

timestamps = []

#creat a list with 'note timestamps' in 16th at which we should play the sample
timestamps16th = [0, 2, 4, 8, 11]

print ("how many times do you wanna play?")
playtimes = input()
playtimes = int(playtimes)


#transform the sixteenthTimestamps to a timestamps list with time values
for timestamp in timestamps16th:
#timestamps16th = float(timestamps16th)
	timestamps.append(timestamp*sixteenthNoteDuration) 



def playsequence (timestampssequence):
#play the sequence

	#retrive first timestamp
	timestamp = timestampssequence.pop(0)
	startTime = time.time()
	keepPlaying = True
	while keepPlaying:
		currentTime = time.time()
		if(currentTime - startTime >= timestamp):
			#playsample
			samples[0].play()
			random.shuffle(samples)
			
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




	
for i in range(playtimes):
	playsequence(timestamps.copy())

