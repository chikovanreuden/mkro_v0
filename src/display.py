import board
import busio
import adafruit_ssd1306

class Display:
    line_height = 8
    line_char_max = 21
   
    def __init__(self) -> None:
        self.lines = [""] * 10
        SCL = board.GP1
        SDA = board.GP0
        i2c = busio.I2C(SCL, SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        self.display.fill(0)
        self.display.show()
    
    def update( self ):
        self.display.fill(0)
        idx = 0
        for line in self.lines:
        # for idx, line in enumerate( self.lines ):
            # self.display.text( line , 0, ( 8 * (idx + 1) ) - 8, 1 )
            self.display.text( line , 0, 8 * idx , 1 )
            idx += 1
        self.display.show()
    
    def update_line( self, line_num, text):
        if ( line_num > 8 ):
            raise ValueError('line_num has to be between 1 and 6.')
        self.lines[ line_num - 1 ] = text