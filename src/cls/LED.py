import board
class LED:
    def __init__(self, color, gpio, usage):
        self.color = color
        self.gpio = gpio
        self.usage = usage
        self.pin = None
    def __repr__(self):
      return f"LED('{self.color}')"

leds = [
    LED( "white", board.GP17, "profileindicator"),
    LED( "blue", board.GP16, "profileindicator"),
    LED( "green", board.GP14, "profileindicator"),
    LED( "yellow", board.GP15, "profileindicator")
]