from adafruit_motorkit import MotorKit
from time import sleep

kit = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)

from adafruit_motor import stepper

for i in range(1000):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)

sleep(5)

for i in range(1000):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)

sleep(5)

for i in range(1000):
        kit2.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)

sleep(5)

for i in range(1000):
        kit2.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)

sleep(5)






