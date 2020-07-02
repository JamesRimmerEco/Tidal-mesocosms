import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

from adafruit_motor import stepper

for i in range(4000):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)



