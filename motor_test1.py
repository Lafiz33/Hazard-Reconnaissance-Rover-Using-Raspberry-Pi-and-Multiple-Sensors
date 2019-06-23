import RPi.GPIO as GPIO
import time
import curses
screen=curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

GPIO.setmode(GPIO.BCM)

m1a=6
m1b=13

m2a=19
m2b=26

GPIO.setup(m1a,GPIO.OUT)
GPIO.setup(m1b,GPIO.OUT)

GPIO.setup(m2a,GPIO.OUT)
GPIO.setup(m2b,GPIO.OUT)


try:
	while True:
		char=screen.getch()
		if char== ord('q'):
			break
		elif char == curses.KEY_UP:
			GPIO.output(m1a, True)
			GPIO.output(m1b, False)
			GPIO.output(m2a, True)
			GPIO.output(m2b, False)
			print "up"

		elif char==curses.KEY_DOWN:
			GPIO.output(m1a, False)
			GPIO.output(m1b, True)
			GPIO.output(m2a, False)
			GPIO.output(m2b, True)
			print "down"
		elif char==curses.KEY_RIGHT:
			GPIO.output(m1a, False)
			GPIO.output(m1b, True)
			GPIO.output(m2a, True)
			GPIO.output(m2b, False)
			print "left"
		elif char==curses.KEY_LEFT:
			GPIO.output(m1a, True)
			GPIO.output(m1b, False)
			GPIO.output(m2a, False)
			GPIO.output(m2b, True)
			print "right"
		else:
			GPIO.output(m1a, False)
			GPIO.output(m1b, False)
			GPIO.output(m2a, False)
			GPIO.output(m2b, False)
finally:
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
	GPIO.cleanup()
