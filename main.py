from luma.core.interface.serial import spi
from luma.lcd.device import st7735
from PIL import Image, ImageDraw, ImageFont
import time

serial = spi(
    port=0,
    device=0,
    gpio_DC=22,
    gpio_RST=18,
    bus_speed_hz=16000000
)

device = st7735(
    serial,
    width=128,
    height=160,
    rotate=0
)

img = Image.new("RGB", (128, 160), "black")
draw = ImageDraw.Draw(img)

draw.rectangle((0, 0, 127, 159), outline="white")
draw.text((10, 20), "Hello Jetson!", fill="green")
draw.text((10, 50), "ST7735 TFT", fill="yellow")
draw.text((10, 80), "128x160", fill="cyan")

device.display(img)

time.sleep(10)