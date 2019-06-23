import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

AA=25
GPIO.setup(25,GPIO.IN)
print "Starting sensor"

while True:
	if GPIO.input(25)==1:
		print ("Gas alart")
	else:
		print ("No Gas")
	time.sleep(1)

GPIO.cleanup()
