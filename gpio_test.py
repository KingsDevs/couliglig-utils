import board
import digitalio
import time

print("Creating pins...")

dc = digitalio.DigitalInOut(board.D22)
dc.direction = digitalio.Direction.OUTPUT

rst = digitalio.DigitalInOut(board.D18)
rst.direction = digitalio.Direction.OUTPUT

cs = digitalio.DigitalInOut(board.CE0)
cs.direction = digitalio.Direction.OUTPUT

print("Toggling...")
while True:
    dc.value = True
    rst.value = True
    cs.value = True
    time.sleep(1)

    dc.value = False
    rst.value = False
    cs.value = False
    time.sleep(1)