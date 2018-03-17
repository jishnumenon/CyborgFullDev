import serial
import subprocess
import os

#Set number

theSetNo = 1

# all serial data initialised
serialSensor = serial.Serial('/dev/ttyACM0','115200')


def theTentOrButton(nowSerial):
	#Check if the serial data is from the Tentacle or Button press
	print "Checking what type of serial command"
	# Return 1 if a Tentacle is hit.
	# Return 2 if a Button is pressed.
	# Return 0 if serial data is invalid
	
	if (nowSerial.split("%")[1] == 'T'):
		serialCommand = 1
		print ("A tentacle has been Hit ")
	elif (nowSerial.split("%")[1] == 'B'):
		serialCommand = 2
		print ("A button has been pressed")
	else:
		print ("Unexpected Serial Data")
		serialCommand = 0
	return serialCommand

def findTent(tentNo):
	tentNo.split("%")[2].split(":")[1]
	
#################################################################################
# Play tentacle Sounds

def tentacle1Play():
	print ("Play tentacle 1 sound ,set " + str(theSetNo)+"\n")
	subprocess.Popen(["aplay","/home/pi/Desktop/Cyborg/audio/SET1/T4I0S1.wav"])
def tentacle2Play():
        print ("Play tentacle 2 sound ,set " + str(theSetNo))

def tentacle3Play():
        print ("Play tentacle 3 sound ,set " + str(theSetNo))

def tentacle4Play():
        print ("Play tentacle 4 sound ,set " + str(theSetNo))

def tentacle5Play():
        print ("Play tentacle 5 sound ,set " + str(theSetNo))
#################################################################################

def triggered(tent,set):
	filename = "T"+str(tent)+"I0"+"S"+str(set)+".wav"
	print filename 

os.system("aplay startup.wav")
while 1:
	theSerial = serialSensor.readline()
	print theSerial
	if( theTentOrButton(theSerial) == 1):
		tent = theSerial.split("%")[2].split(":")[1]
		set = theSerial.split("%")[4].split(":")[1]
		print "tent : "+str(tent)
		print "set : "+str(set)
		filePath = "audio/"+"SET"+str(set)+"/"
		fileName = "T"+str(tent)+"I0"+"S"+str(set)+".wav"
		subprocess.Popen(["aplay",str(filePath+fileName)]) 
		
	elif ( theTentOrButton(theSerial) == 2):
		theSetNo = theSerial.split("%")[2].split(":")[1]
		print "Buton Handling \n"
	elif ( theTentOrButton(theSerial) == 0):
		print "Invalid Serial Data"
	else :
		print "Logical error in infinite while loop"
	
	
