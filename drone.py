
##AUTHOR: KORRE D. HENRY
### DESCRIPTION: THIS program, when allowed network access can manually fly a tello drone using network packets as well as USER instruction.
### Fly Drone
import os
import sys
import time 
import tellopy
import socket
import tellopy
from pynput import keyboard

##Allows to the organization of imported tellopy module
def handler(event, sender, data, **args):
    global drone
    drone = sender

def controls (key):
    ''' Performs basic funtionalities of drone flight capibility'''
    if str (key) == 'Key.up': ##UP ARROW
        print ("UP")
        drone.forward (20)

    elif str (key) == 'Key.down':## DOWN ARROW
        drone.backward (20)
    elif str (key) == 'Key.left': ## LEFT ARROW
        drone.left (20)
    elif str (key) == 'Key.right': ## RIGHT ARROW
        drone.right (20)
    elif str (key) == 'Key.space': ## SPACE BAR
        '''Sends packet to make the drone takeoff'''
        drone.takeoff ()
    elif str (key) == 'Key.delete': ## DELETE KEY
        '''Sends packet to make drone land'''
        drone.land ()
    elif str (key)== 'key.enter': ## ENTER KEY
        drone.up (20)
    elif str (key) == 'key.shift_r': ## Right SHIFT KEY
        drone.down (20)
    elif str (key) == '<177>': ## F4 KEY
        drone.flip_forward ()
    elif str (key) == '<179>': ## F5 KEY
       drone.flip_back () 
    elif str (key)== 'Key.shift_l': ## LEFT SHIFT KEY
        '''Stops reciveing network packets to fly, unless it's to land.'''
        drone.quit ()
        
'''These two relating functions below are used to satify the keyboard listener
imported from pynput's keyboard
'''
def on_press (key):
    pass
def on_release (key):
    '''Once the key is realesed it calls the controls () function with the 'key' parm'''
    controls (key)

def connection ():
    #drone = tellopy.Tello()
    #drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
    #drone.connect()
    print ('Looking for Drone...\n>>')
    #drone.wait_for_connection(60.0)
    #drone.set_pitch(0.5)

connection ()

'''Moniters when keys are pressed and released'''
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

