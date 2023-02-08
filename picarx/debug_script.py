"Debug Script for Picar-X"

from picarx_improved import Picarx


Picarx.set_dir_servo_angle(0)
Picarx.forward
"Debug Script for Picar-X"

from picarx_improved import Picarx
import time
import logging

Chad = Picarx()

def parallel_parking_right():
    Chad.set_dir_servo_angle(0)
    time.sleep(1)
    Chad.forward(25)
    time.sleep(1)
    Chad.stop()
    time.sleep(1)
    Chad.set_dir_servo_angle(30)
    time.sleep(0.75)
    Chad.backward(10)
    time.sleep(0.75)
    Chad.set_dir_servo_angle(-30)
    time.sleep(0.75)
    Chad.stop()
    Chad.set_dir_servo_angle(0)
    time.sleep(1)
    Chad.forward(10)
    time.sleep(0.25)
    Chad.stop()

def parallel_parking_left():
    Chad.set_dir_servo_angle(0)
    time.sleep(1)
    Chad.forward(25)
    time.sleep(1)
    Chad.stop()
    time.sleep(1)
    Chad.set_dir_servo_angle(-30)
    time.sleep(0.75)
    Chad.backward(10)
    time.sleep(0.75)
    Chad.set_dir_servo_angle(30)
    time.sleep(0.75)
    Chad.stop()
    Chad.set_dir_servo_angle(0)
    time.sleep(1)
    Chad.forward(10)
    time.sleep(0.25)
    Chad.stop()

def leave_spot_going_left():
    Chad.set_dir_servo_angle(-30)
    time.sleep(0.5)
    Chad.forward(10)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(30)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(0)
    time.sleep(0.25)
    Chad.forward(40)
    time.sleep(1)
    Chad.stop()

def leave_spot_going_right():
    Chad.set_dir_servo_angle(30)
    time.sleep(0.5)
    Chad.forward(10)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(-30)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(0)
    time.sleep(0.25)
    Chad.forward(40)
    time.sleep(1)
    Chad.stop()

def three_point_turn_right():
    Chad.set_dir_servo_angle(0)
    time.sleep(0.5)
    Chad.forward(30)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(35)
    time.sleep(0.5)
    Chad.forward(15)
    time.sleep(0.5)
    Chad.stop()
    time.sleep(0.75)
    Chad.set_dir_servo_angle(-15)
    time.sleep(0.75)
    Chad.stop()
    time.sleep(0.75)
    Chad.backward(10)
    time.sleep(1)
    Chad.stop()
    time.sleep(0.25)
    Chad.set_dir_servo_angle(45)
    time.sleep(0.75)
    Chad.forward(15)
    time.sleep(0.75)
    Chad.set_dir_servo_angle(0)
    time.sleep(0.5)
    Chad.forward(40)
    time.sleep(1)
    Chad.stop()

def three_point_turn_left():
    Chad.set_dir_servo_angle(0)
    time.sleep(0.5)
    Chad.forward(30)
    time.sleep(0.5)
    Chad.set_dir_servo_angle(-35)
    time.sleep(0.5)
    Chad.forward(15)
    time.sleep(0.5)
    Chad.stop()
    time.sleep(0.75)
    Chad.set_dir_servo_angle(15)
    time.sleep(0.75)
    Chad.stop()
    time.sleep(0.75)
    Chad.backward(10)
    time.sleep(1)
    Chad.stop()
    time.sleep(0.25)
    Chad.set_dir_servo_angle(-45)
    time.sleep(0.75)
    Chad.forward(15)
    time.sleep(0.75)
    Chad.set_dir_servo_angle(0)
    time.sleep(0.5)
    Chad.forward(40)
    time.sleep(1)
    Chad.stop()

three_point_turn_left()



