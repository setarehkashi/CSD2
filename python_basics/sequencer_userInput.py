import simpleaudio as sa 
import time
import random



samples = [sa.WaveObject.from_wave_file("snare.wav"),
           sa.WaveObject.from_wave_file("kick.wav")]


bpm = 120
print ("default bpm: 120")

print ("what bpm do you wanna play with? please keep in mind you can only use intergers as a bpm value!")
bpm = input()
bpm = int(bpm)
#calculate the duration of a quarternote
quarterNoteDuration = 60 / bpm
#calculate the duration of a SixteenthNote
sixteenthNoteDuration = quarterNoteDuration / 4.0

timestamps = []

print ("how many times do you wanna play?")
playtimes = input()
playtimes = int(playtimes)



def askuserfortimestamps16th (timestamps): 
	print ("please give a list of intergers, this will be used as timestamps in 16th")
	for s in range(playtimes):
		
		timestamp16th = input()
		timestamp16th = int(timestamp16th)
		
		timestamps.append(timestamp16th * sixteenthNoteDuration)
	return timestamps

#creat a list with 'note timestamps' in 16th at which we should play the sample
#timestamps16th = [0, 2, 4, 8, 11]
askuserfortimestamps16th (timestamps)



#transform the sixteenthTimestamps to a timestamps list with time values
#for timestamp in timestamps16th:
	#timestamps16th = float(timestamps16th)
	#timestamps.append(timestamp*sixteenthNoteDuration) 

def TimestampstoDuration (timestamp16th):
	#duration functie maakt van timestamos16th een duratielijst 
	#transform the sixteenthTimestamps to a timestamps list with time values
	#timestamps.append(timestamp*sixteenthNoteDuration)
	for waarde in timestamps:
		timestamps.append(timestamps16th)

# functie timestam
print (timestamps)

#timestamps16th = input()
#print ("timestamps16th",timestamps16th)
#timestamps16th = int(timestamps16th)
#TimestampstoDuration (timestamps16th,bpm)

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

print ("well done")

