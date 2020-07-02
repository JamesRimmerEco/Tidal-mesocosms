import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

from adafruit_motor import stepper

for i in range(450):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)






