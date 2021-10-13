import joystick
import time

address = 0x48
analog = joystick.Joystick(address)

try:
  while True:
    x_value = analog.getX()
    y_value = analog.getY()
    print(x_value + ', ' + y_value)
    time.sleep(0.1)

except KeyboardInterrupt:
  print("Exiting")
