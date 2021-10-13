import joystick
import time
a = 1
address = 0x48
analog = joystick.Joystick(address)

while a > 0 :
  x_value = getX()
  y_value = getY()
  print(x_value + ', ' + y_value)
