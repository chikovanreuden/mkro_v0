import time
import board
import digitalio
import usb_hid
import json
from adafruit_hid.keyboard import Keyboard
from adafruit_debouncer import Debouncer

from src.cls.Key import keys, matrix
from src.cls.LED import leds
from src.cls.Profile import Profile
from src.cls.display import Display

display = Display()

with open('./src/config/local.json') as localJson:
    data = json.load(localJson)
    print(data)

kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

def change_led():
    b = Profile.get_current_profile_binary()
    b = ''.join( reversed( b ) )
    for idx in range( len( Profile.profiles ) ):
        if ( b [ idx ] == "1" ):
            leds[ idx ].pin.value = True
        else:
            leds[ idx ].pin.value = False

def change_display():
    change_led()
    rows = [""] * 4
    idz = 0
    for row in matrix:
        for k in row:
            
            rows[idz] += " " + '{: <4}'.format(k.name[:4])
        idz += 1
    display.header = "Chiko Makro V0"
    display.subheader = "Profile " + str( Profile.current ) 
    display.lines = rows
    display.update()
    
for led in leds:
    led.pin = digitalio.DigitalInOut( led.gpio )
    led.pin.direction = digitalio.Direction.OUTPUT
    led.pin.value = True
time.sleep( 0.2 )
for led in leds:
    led.pin.value = False

for k in keys:
    k.pin = digitalio.DigitalInOut( k.gpio )
    k.pin.direction = digitalio.Direction.INPUT
    k.pin.pull = digitalio.Pull.UP
    k.switch = Debouncer(k.pin)

Profile( "Profile Uno" )
Profile( "Profile Two" )

change_led()
change_display()

while True:
    for k in keys:
        k.switch.update()
        if ( k.switch.fell ):
            print( k.name + ' pressed' + " | Profile: " + str( Profile.current ) + " | Layer: " + str( Profile.current-1 ))
            if ( k.type == "profileswitcher" ):
                newProf = Profile.next()
                change_led()
                change_display()
            if ( k.type == "key"):
                if ( k.key and ( len( k.key ) > ( Profile.current -1 ) ) ):
                    for kk in k.key[ Profile.current-1 ]:
                        kbd.press( kk )
            k.last_pressed = time.monotonic()
        if ( k.switch.rose ):
            print( k.name + ' released' + " | Profile: " + str( Profile.current ) + " | Layer: " + str( Profile.current-1 ))
            if ( k.type == "key" ):
                if ( k.key and ( len( k.key ) > ( Profile.current -1 ) ) ):
                    for kk in reversed( k.key[ Profile.current-1 ] ):
                        kbd.release( kk )