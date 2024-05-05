import board
import busio
import adafruit_ssd1306

SCL = board.GP1
SDA = board.GP0
i2c = busio.I2C(SCL, SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
# display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

display.fill(0)
display.show()

display.text('ChikoMkroV1', 0, 0, 1)
display.text('Profile: X', 0, 8, 1 )
display.text('Profile: X', 0, 16, 1 )
display.text('Profile: X', 0, 24, 1 )
display.text('Profile: X', 0, 32, 1 )
display.text('Profile: X', 0, 40, 1 )
# .invert(True).invert(True)
display.show()

class Display:
    def __init__(self) -> None:
        pass
    def update():
        pass