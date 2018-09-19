import simpleaudio as sa

print ("how many times do you wanna play house practice.wav?")
 
times = int(input('>> '))
while(times>0) :
	times = times-1
	wave_obj = sa.WaveObject.from_wave_file("house practice.wav")
	play_obj = wave_obj.play()
	play_obj.wait_done()

