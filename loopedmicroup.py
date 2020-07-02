import time
from adafruit_motorkit import MotorKit
from time import sleep

kit = MotorKit()

from adafruit_motor import stepper

for a in range(2):
    for i in range(2000):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
        sleep(2)

