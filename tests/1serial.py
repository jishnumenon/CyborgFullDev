import serial
serialSensor =serial.Serial('/dev/ttyACM0', '115200')
while 1:
        print (serialSensor.readline())


