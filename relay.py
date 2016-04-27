#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys

class Relay():
   def __init__(self):
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      self.relay = [0,18,23,24,25]

      # Set relay pins as output
      GPIO.setup(self.relay[1], GPIO.OUT)
      GPIO.setup(self.relay[2], GPIO.OUT)
      GPIO.setup(self.relay[3], GPIO.OUT)
      GPIO.setup(self.relay[4], GPIO.OUT)

   def liga(self, id):
      GPIO.output(self.relay[id], GPIO.LOW)
  
   def desliga(self, id):
      GPIO.output(self.relay[id], GPIO.HIGH)

      
msg = '''
   Execute assim:
      relay params1 params1, sendo:
        params1 o numero do relay 1,2,3 ou 4
        params2 o estado on ou off 
    '''


horta = Relay()
relay = sys.argv[1]
estado  = sys.argv[2]

if not relay in ['1','2','3','4']:
   print(msg) 
   exit(1)
if estado == "on":
   horta.liga(int(relay))
elif estado == "off":
   horta.desliga(int(relay))
else:
   print(msg) 

