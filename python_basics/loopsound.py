import simpleaudio as sa 
import time

	
print ("how many times do you wanna play snare.wav ?")
playtimes = input()
playtimes = int(playtimes)
ritmelijst = [] 
for  s  in range(playtimes):
	ritmewaarde = input()
	ritmewaarde = float(ritmewaarde) #maakt een float van input hierboven
	ritmelijst.append(ritmewaarde)#voegt gegeven ritme aan me ritmelijst toe
	print (ritmelijst)
#ritmelijst is een lijst van floats die ritmes bevat
print (" what bpm do you wanna play snare.wav with?")
bpm = input()
bpm = int(bpm)
#print ("bpm = " + str(bpm)) Oom te testen of het klopt 

durationLijst = []
for waarderitmelijst in ritmelijst:
	duratiekwartnoot = 60/bpm 
	duratieWaarde = duratiekwartnoot * waarderitmelijst
	durationLijst.append(duratieWaarde)

def playSample(sample, duration) :
	wave_obj = sa.WaveObject.from_wave_file(sample)
	play_obj = wave_obj.play()
	time.sleep(duration)

for n in durationLijst: #n voor iedere variable in durationlijst 
	playSample("snare.wav", n)
	

print(durationLijst)

