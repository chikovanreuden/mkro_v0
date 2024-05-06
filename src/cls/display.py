import board
import busio
import adafruit_ssd1306

class Display:
    line_height = 8
    line_char_max = 21

    def __init__( self ) -> None:
        self.header = ""
        self.subheader = ""
        self.lines = [""] * 4
        SCL = board.GP1
        SDA = board.GP0
        i2c = busio.I2C(SCL, SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        self.display.fill(0)
        self.display.show()
    
    def update( self ):
        self.display.fill(0)
        self.display.text( self.header , 0, 0 , 1 )
        self.display.text( self.subheader , 0, 8 , 1 )
        idx = 21
        for line in self.lines:
            self.display.text( line , 0, idx , 1 )
            idx += 8+4
        self.display.show()