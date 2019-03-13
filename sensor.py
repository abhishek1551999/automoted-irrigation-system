import sys
import Adafruit_DHT
import time
import requests
from time import sleep
import mcp3008
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)


TRIG = 26                                  #Associate pin 26 to TRIG
ECHO = 16 				   #Associate pin 16 to ECHO


GPIO.setup(TRIG,GPIO.OUT)             
GPIO.setup(ECHO,GPIO.IN)


url="http://192.168.43.167:8086/temperature/get"
def Temp():
	while True:
		
		m = (5)
		m = (m*100)/1024
		humidity, temperature = Adafruit_DHT.read_retry(11,4)
		GPIO.output(TRIG, False)
        	GPIO.output(TRIG, True)
        	time.sleep(0.00001)               
        	GPIO.output(TRIG, False)  
        	while GPIO.input(ECHO)==0:
            		pulse_start = time.time()        
        	while GPIO.input(ECHO)==1:            
            		pulse_end = time.time()  
        	pulse_duration = pulse_end - pulse_start
mcp3008.readadc
        	distance = pulse_duration * 17150        
        	distance = round(distance, 2)
		distance = 15 - distance
		r = mcp3008.readadc(0)
		GPIO.output(21,False)
		if (m<60 and r<10) :
			GPIO.output(21, True)
			#time.sleep(3)
			#GPIO.output(21,False)
        	else :
			GPIO.output(21,False)
		print temperature
		print humidity
		print "Moisture level: {:>5} ".format(m)
        	print distance
		print r
		if(r<10):
			stat="Not Raining"
		else:	
			stat = "Raining"
		data={'temperature':temperature , 'humidity' : humidity,'moisture':m , 'level':distance ,'rain' : stat}
		requests.get(url,params=data)
		time.sleep(1)
Temp()
