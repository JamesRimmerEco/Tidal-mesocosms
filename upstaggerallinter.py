from adafruit_motorkit import MotorKit
from time import sleep

kit1 = MotorKit(address=0x60)
kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)

from adafruit_motor import stepper
for j in range(6):
    for i in range(100):
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit2.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit2.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit3.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        
    print("Turn %s" % (j + 1))

    sleep(5)