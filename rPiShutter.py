import socket
import sys
from struct import *
import RPi.GPIO as GPIO

#Set Up IP Addresses
self_IP = "169.230.188.46"
self_PORT = 2424

time.sleep(10)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock.bind((self_IP,self_PORT))

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.output(7,false)
GPIO.output(8,false)

while True:
	data, addr =sock.recvfrom(1024)
	buffer = data.decode()
	print("running", buffer)
	if (buffer==0):
		GPIO.output(7,false)
		GPIO.output(8,false)
	elif(buffer==1):
		GPIO.output(7,true)
		GPIO.output(8,false)
	elif(buffer==2):
		GPIO.output(7,false)
		GPIO.output(8,true)
	elif(buffer==3):
		GPIO.output(7,true)
		GPIO.output(8,true)
	else:
		print("invalid")
