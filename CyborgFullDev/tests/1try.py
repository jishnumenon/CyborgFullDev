import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("snareNew2.wav")
pygame.mixer.music.play()
a=pygame.mixer.Sound('snareNew2.wav')
while 1:
	This = raw_input("Enter the Drum number : ")
	if (This == '1'):
		a.play()
	else :
		print ("Invalid")
