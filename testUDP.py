import socket
from struct import *


self_IP = "10.60.114.64"
#self_IP = "10.131.48.204"
self_PORT = 8936
#send_IP ="128.218.19.234"
send_IP = "169.230.188.48"
send_PORT = 8888


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((self_IP, self_PORT))
running = True
buffer = "start"
sock.sendto(buffer.encode(),(send_IP,send_PORT))
print("listening")
while running:
	try:

		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		data = unpack('hhhh',data)
		print ( "received message:", data)
	except(KeyboardInterrupt, SystemExit):
		#buffer = "swap"
		#sock.sendto(buffer.encode(),(send_IP,send_PORT))
		print("stopping testUDP")
		buffer ="stop"
		sock.sendto(buffer.encode(), (send_IP,send_PORT))
		sock.close
		running =False
		


