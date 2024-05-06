import board
from adafruit_hid.keycode import Keycode
class Key:
    def __init__(self, name, gpio, type, key):
        self.name = name
        self.gpio = gpio
        self.type = type
        self.key = key
        self.last_pinstate = 1
        self.last_pressed = 0
        self.pin = None
        self.switch = None
    def __repr__(self):
      return f"Key('{self.name}','{self.type}')"

keys = [
    Key( "F13", board.GP5, "key", [ [ Keycode.F13 ] ] ),
    Key( "F14", board.GP13, "key", [ [ Keycode.F14 ] ] ),
    Key( "F15", board.GP18, "key", [ [ Keycode.F15 ] ] ),
    Key( "F16", board.GP9, "key", [ [ Keycode.F16 ] ] ),
    Key( "F17", board.GP4, "key", [ [ Keycode.F17 ] ] ),
    Key( "F18", board.GP12, "key", [ [ Keycode.F18 ] ] ),
    Key( "F19", board.GP19, "key", [ [ Keycode.F19 ] ] ),
    Key( "F20", board.GP8, "key", [ [ Keycode.F20 ] ] ),
    Key( "F21", board.GP3, "key", [ [ Keycode.F21 ] ] ),
    Key( "F22", board.GP11, "key", [ [ Keycode.F22 ] ] ),
    Key( "F23", board.GP20, "key", [ [ Keycode.F23 ] ] ),
    Key( "F24", board.GP7, "key", [ [ Keycode.F24 ], [ Keycode.CONTROL, Keycode.A ] ],  ),
    Key( "mkr1", board.GP2, "profileswitcher", None ),
    Key( "mkr2", board.GP10, "profileswitcher_next", None ),
    Key( "mkr3", board.GP21, "profileswitcher_previous", None ),
    Key( "mkr4", board.GP6, "key", None ),
]