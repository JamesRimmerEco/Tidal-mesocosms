import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

from adafruit_motor import stepper

for i in range(10):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
