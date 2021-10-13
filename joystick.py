import PCF8591 as adc 

class Joystick:
  def __init__(self,address):
    self.value = adc.PCF8591(address)
  def getX(self):
    return self.value.read(2)
  def getY(self):
    return self.value.read(1)


