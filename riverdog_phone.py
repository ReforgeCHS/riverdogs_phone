import os
import time
import datetime
import random
import dircache
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dir = 'test_audio'
pygame.mixer.init()
delay = 2

print '''
===================================
Starting Reforge / Riverdogs Phone Booth App
==================================
'''

def select_audio_file(dir):
	filename = random.choice(dircache.listdir(dir))
	path = os.path.join(dir, filename)
	print '[+]-> Grabbed file: ' + path
	return(path)

def play_audio(audio_file):
	pygame.mixer.music.load(audio_file)
	print '[+]-> Playing (' + str(delay) + ' Sec Delay): ' + audio_file
	time.sleep(delay)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

def main():
	print '[+]-> Starting at ' + str(datetime.datetime.now())
	print '[+]-> Waiting for action...'
	while True:
		input_state = GPIO.input(18)
		if input_state == False:
			print '[+]-> Action Detected! @ (' + str(datetime.datetime.now()) + ')'
			play_audio(select_audio_file(dir))
			time.sleep(0.2)
			print '[+]-> Waiting for action...'

if __name__ == "__main__":
	main()
