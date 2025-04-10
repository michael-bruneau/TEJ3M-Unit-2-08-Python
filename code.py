# Created by: Michael Bruneau
# Created on: April 2025
#
# This module is a Raspberry Pi Pico program that turns Micro Servo if an object gets within 50cm of the Ultrasonic Distance Sensor


import time
import board
import adafruit_hcsr04
import digitalio
import pwmio
from adafruit_motor import servo
import analogio


# variables and constants
servo_delay = 2
UNIT_ANGLE = 0.0027
servo_angle = 0
biggest_angle = 0
wiper_output = 0

# setup
potentiometer = analogio.AnalogIn(board.GP26)

# create a PWMOut object on Pin GP12.
pwm = pwmio.PWMOut(board.GP12 , duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# loop
while True:
    # get wiper output
    wiper_output = potentiometer.value

    # calculates angle
    servo_angle = wiper_output * UNIT_ANGLE

    # turns servo
    my_servo.angle = servo_angle
    time.sleep(servo_delay)
