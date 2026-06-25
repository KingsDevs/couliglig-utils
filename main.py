import time
import board
import digitalio
from PIL import Image, ImageDraw
from adafruit_rgb_display import st7735

spi = board.SPI()

cs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
reset = digitalio.DigitalInOut(board.D18)

display = st7735.ST7735R(
    spi,
    cs=cs,
    dc=dc,
    rst=reset,
    width=128,
    height=160,
    rotation=0,
)

image = Image.new("RGB", (128, 160), "black")
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, 127, 159), outline="white")
draw.text((10, 20), "Hello Jetson", fill="green")
draw.text((10, 50), "ST7735 TFT", fill="yellow")

display.image(image)

time.sleep(10)