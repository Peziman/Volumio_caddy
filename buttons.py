#=====================================#
# Author: Julien Croteau              #
# Created: 08/01/2018                 #
#=====================================#
import  RPi.GPIO as GPIO
import time
import os
import subprocess
from socketIO_client import SocketIO, LoggingNamespace


class Buttons(object): # creates a class for declaring buttons
    def __init__(self, pin, command, longpress):
        self.pin = pin
        self.command = command
        self.longpress = longpress
        self.io = SocketIO('localhost', 3000) # WebsocketIO connection, way faster than the command prompt
        GPIO.setup(self.pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, bouncetime=1000) 
        if (self.longpress): # Sets callback function for buttons with longpress action
            GPIO.add_event_callback(self.pin, self.longpressFn)
        else : # Sets callback function for buttons without longpress action
            GPIO.add_event_callback(self.pin, self.norm)
    
    def norm(self, channel): # callback function for buttons without longpress action
        self.io.emit(self.command)
                
    def longpressFn(self, channel): # callback function for button with longpress action
        delay = 0 
        for i in range(52): # count from 1 to 5.2 seconds when button is maintained
            delay = delay + 1
            time.sleep(0.1)
            if (GPIO.input(self.pin)): # When button is released, go on.
                break
        if (delay > 50): # If delay is longer than 5 seconds, do longpress action
            os.system(self.longpress)
        else: # else do short press action
            self.io.emit(self.command)
            
class Rotary(Buttons):
    ''' Class for rotary encoders that inherits from button class '''
    def __init__(self, pin, command, longpress, pinA, pinB):
        super(Rotary, self).__init__(pin, command, longpress)
        self.pinA = pinA
        self.pinB = pinB
        GPIO.setup(self.pinA, GPIO.IN,pull_up_down=GPIO.PUD_UP) # Rotary input A
        GPIO.setup(self.pinB, GPIO.IN,pull_up_down=GPIO.PUD_UP) # Rotary input B
        GPIO.add_event_detect(self.pinA, GPIO.FALLING, bouncetime=1) # Seting up both pins as if they were push buttons
        GPIO.add_event_callback(self.pinA, self.pinAFalling)
        GPIO.add_event_detect(self.pinB, GPIO.FALLING, bouncetime=1)
        GPIO.add_event_callback(self.pinB, self.pinBFalling)
        
    def pinAFalling(self,channel):
        if GPIO.input(self.pinA)==False and GPIO.input(self.pinB)==False: # if pin A then pin B
            os.system('volumio volume plus') # for the volume the os command is more reliable
            
    def pinBFalling(self,channel):
        if GPIO.input(self.pinB)==False and GPIO.input(self.pinA)==False: # if pin B then pin A
            os.system('volumio volume minus')
        


        
                