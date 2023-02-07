#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
left_color = ColorSensor(Port.S2)
right_color = ColorSensor(Port.S1)
left_sonic = UltrasonicSensor(Port.S3)
gyro = GyroSensor(Port.S4)



# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=122)
def stop():
    robot.stop()
    left_motor.brake()
    right_motor.brake()

# Write your program here.
while True:
    robot.drive(500, 0)
    if left_color.reflection() <= 8:
        robot.stop()
        while left_color.reflection() <= 8:
            left_motor.brake()
            right_motor.run(1000)
    if right_color.reflection() <= 8: 
        robot.stop()
        while right_color.reflection() <= 8:
            left_motor.run(1000)
            right_motor.brake()
        