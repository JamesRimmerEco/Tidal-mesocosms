from adafruit_motorkit import MotorKit
from time import sleep

kit = MotorKit()

from adafruit_motor import stepper
for j in range(6):
    for i in range(20):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)

    print("Turn %s" % (j + 1))

    sleep(10)