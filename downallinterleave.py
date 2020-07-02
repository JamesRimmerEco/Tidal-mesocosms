from adafruit_motorkit import MotorKit

# Initialise the first hat on the default address

kit1 = MotorKit(address=0x60)

# Initialise the second hat on a different address

kit2 = MotorKit(address=0x61)
kit3 = MotorKit(address=0x62)

import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

from adafruit_motor import stepper

for i in range(400):
    kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    kit2.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    kit3.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    kit3.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)











