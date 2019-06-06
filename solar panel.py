# ~ import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time

# ~ GPIO.setmode(GPIO.BCM)
# ~ GPIO.setup(4,GPIO.IN)
# ~ GPIO.setup(17,GPIO.IN)
# ~ GPIO.setup(25,GPIO.IN)
# ~ GPIO.setup(27,GPIO.IN)

#S1-NW sensor; S2 - NE sensor; S3 - SW sensor; s4 - SE sensor
# ~ S1 = GPIO.input(4)
# ~ S2 = GPIO.input(17)
# ~ S3 = GPIO.input(25)
# ~ S4 = GPIO.input(27)
def printing(AVT,AVB,AVL,AVR):
	print("This is the average top...",AVT)
	print("This is the average bottom...",AVB)
	print("This is the average left...",AVL)
	print("This is the average right...",AVR)
	

while True:
	Sensor1 = input("S1\n")
	Sensor2 = input("S2\n")
	Sensor3 = input("S3\n")
	Sensor4 = input("S4\n")
	
	S1 = int(Sensor1)
	S2 = int(Sensor2)
	S3 = int(Sensor3)
	S4 = int(Sensor4)

	AVT = S1+S2
	AVB = S3+S4
	AVL = S1+S3
	AVR = S2+S4
	
	
	if AVT > AVB:
		while AVT > AVB:
			print("Rotating up")
			time.sleep(1)
			S3 += 1
			S4 += 1
			AVT = S1+S2
			AVB = S3+S4
			AVL = S1+S3
			AVR = S2+S4
		
	elif AVB > AVT:
		while AVB > AVT:
			time.sleep(1)
			print("Rotating down")
			S1 += 1
			S2 += 1
			AVT = S1+S2
			AVB = S3+S4
			AVL = S1+S3
			AVR = S2+S4		
	else:
		print("Sunlight is good in the North and South axis...")
		
	if AVL > AVR:
		while AVL > AVR:
			time.sleep(1)
			print("Rotating left")
			S2 += 1
			S4 += 1
			AVT = S1+S2
			AVB = S3+S4
			AVL = S1+S3
			AVR = S2+S4
	elif AVR > AVL:
		while AVR > AVL:
			time.sleep(1)
			print("Rotating right")
			S1 += 1
			S3 += 1
			AVT = S1+S2
			AVB = S3+S4
			AVL = S1+S3
			AVR = S2+S4
	else:
		print("Sunlight is good in the West and East axis...")
			
			
	


	

