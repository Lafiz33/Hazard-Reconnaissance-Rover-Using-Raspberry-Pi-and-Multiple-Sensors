import RPi.GPIO as GPIO
import time
import curses
screen=curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)        

p=GPIO.PWM(27, 50)
p.start(7.5)
i=7.5
p.ChangeDutyCycle(7.5)
try:
        while True:
		char=screen.getch()
		if char==ord('w'):
			i=i+1
                	p.ChangeDutyCycle(i)
			print i
                	time.sleep(1)
		elif char==ord('s'):
			i=i-1
			p.ChangeDutyCycle(i)
			print i
			time.sleep(1)
except KeyboardInterrupt:
        p.stop()
	curses.endwin()
	curses.echo()
	curses.nocbreak()
	screen.keypad(0)
        GPIO.cleanup()

