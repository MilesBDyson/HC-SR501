#!/usr/bin/env python3

'''
This will help you calibrate the built in timer on the HC-SR501
the time is in seconds and only a reference.
if you need to be more precise, you need to use a stopwatch
it uses GPIO P9_12 as the trigger pin by default
to use a different pin please edit the motion_detector.py file
'''

from time import sleep
import motion_detector

timer = 0

if __name__ == "__main__":
	while True:
		if motion_detector.motion_detect():
			timer = timer + 1
			print( "Motion Detected %ss" % (timer))
		else:
			timer = 0
			print("Clear")
		sleep(1)
