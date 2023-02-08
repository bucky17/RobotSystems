"Debug Script for Picar-X"

from picarx_improved import Picarx
try:
    from robot_hat import *
    from robot_hat import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except ImportError:
    print("This computer does not appear to be a PiCar-X system (robot_hat is not present). Shadowing hardware calls with substitute functions")
    from sim_robot_hat import *

import time
import statistics as st
import logging



class Manuevering(object):

    def __init__(self):
        self.Chad = Picarx()

    def parallel_parking_right(self):
        self.Chad.set_dir_servo_angle(0)
        time.sleep(1)
        self.Chad.forward(25)
        time.sleep(1)
        self.Chad.stop()
        time.sleep(1)
        self.Chad.set_dir_servo_angle(30)
        time.sleep(0.75)
        self.Chad.backward(10)
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(-30)
        time.sleep(0.75)
        self.Chad.stop()
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(0)
        time.sleep(1)
        self.Chad.forward(10)
        time.sleep(0.25)
        self.Chad.stop()

    def parallel_parking_left(self):
        self.Chad.set_dir_servo_angle(0)
        time.sleep(1)
        self.Chad.forward(25)
        time.sleep(1)
        self.Chad.stop()
        time.sleep(1)
        self.Chad.set_dir_servo_angle(-30)
        time.sleep(0.75)
        self.Chad.backward(10)
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(30)
        time.sleep(0.75)
        self.Chad.stop()
        self.Chad.set_dir_servo_angle(0)
        time.sleep(1)
        self.Chad.forward(10)
        time.sleep(0.25)
        self.Chad.stop()

    def leave_spot_going_left(self):
        self.Chad.set_dir_servo_angle(-40)
        time.sleep(0.5)
        self.Chad.forward(10)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(40)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.25)
        self.Chad.forward(40)
        time.sleep(1)
        self.Chad.stop()

    def leave_spot_going_right(self):
        self.Chad.set_dir_servo_angle(40)
        time.sleep(0.5)
        self.Chad.forward(10)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(-40)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.25)
        self.Chad.forward(40)
        time.sleep(1)
        self.Chad.stop()

    def three_point_turn_right(self):
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.5)
        self.Chad.forward(30)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(35)
        time.sleep(0.5)
        self.Chad.forward(15)
        time.sleep(0.5)
        self.Chad.stop()
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(-15)
        time.sleep(0.75)
        self.Chad.stop()
        time.sleep(0.75)
        self.Chad.backward(10)
        time.sleep(1)
        self.Chad.stop()
        time.sleep(0.25)
        self.Chad.set_dir_servo_angle(45)
        time.sleep(0.75)
        self.Chad.forward(15)
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.5)
        self.Chad.forward(40)
        time.sleep(1)
        self.Chad.stop()

    def three_point_turn_left(self):
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.5)
        self.Chad.forward(30)
        time.sleep(0.5)
        self.Chad.set_dir_servo_angle(-35)
        time.sleep(0.5)
        self.Chad.forward(15)
        time.sleep(0.5)
        self.Chad.stop()
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(15)
        time.sleep(0.75)
        self.Chad.stop()
        time.sleep(0.75)
        self.Chad.backward(10)
        time.sleep(1)
        self.Chad.stop()
        time.sleep(0.25)
        self.Chad.set_dir_servo_angle(-45)
        time.sleep(0.75)
        self.Chad.forward(15)
        time.sleep(0.75)
        self.Chad.set_dir_servo_angle(0)
        time.sleep(0.5)
        self.Chad.forward(40)
        time.sleep(1)
        self.Chad.stop()

class GreyScale_Sensing():
    def __init__(self, dark_limit = 600, light_limit = 1400, polarity = 'darker_line', sensitivity = 0.6):
        self.dark_limit = dark_limit
        self.light_limit = light_limit
        self.polarity = polarity

        self.sensitivity = sensitivity

        self.window = 10

        self.means = []

    #def get_line_status(self, sensor_data):

        
def week_2():
    man = Manuevering()

    print("\nWelcome to Driving for Dummies the new interactive driving simulator, mandatory for those who suck at driving!")
    print("\n")
    print("If you are reading this, it is because you are horrible at driving and need training!")
    time.sleep(3)
    
    option = ''

    while option != 'q':
        #Display all choices
        print("\n Press [1] to show how to make a right three-point turn")
        print("\n Press [2] to show how to make a left three-point turn")
        print("\n Press [3] to show how to make a right-handed parallel park")
        print("\n Press [4] to show how to make a left-handed parallel park")
        print("\n Press [5] to show how to leave a parallel park on the right side")
        print("\n Press [6] to show how to leave a parallel park on the left side")
        print("\n Press [q] to quit")

        #Present choices
        option = input("\n What do you suck at most? ")

        if option == '1':
            print("\nI'm not suprised you don't know how to make a three point turn")
            time.sleep(2)
            man.three_point_turn_right()
        elif option == '2':
            print("\nI'm not suprised you don't know how to make a three point turn")
            time.sleep(2)
            man.three_point_turn_left()
        elif option == '3':
            print("\nI bet you hit both the car in front of you and the car behind you, don't you?")
            time.sleep(2)
            man.parallel_parking_right()
        elif option == '4':
            print("\nI bet you hit both the car in front of you and the car behind you, don't you?")
            time.sleep(2)
            man.parallel_parking_left()        
        elif option == '5':
            print("\nOh come on. You have to know how to leave a parking spot.")
            time.sleep(2)
            man.leave_spot_going_left()
        elif option == '6':
            print("\nOh come on. You have to know how to leave a parking spot.")
            time.sleep(2)
            man.leave_spot_going_right()
        elif option == 'q':
            print("\nJust like you to quit when the going gets rough.")
            time.sleep(2)
        else:
            print("\nHAHAHAHAHAHA YOU CAN'T EVEN GET THIS RIGHT") 
            time.sleep(2) 

    time.sleep(2)
    print("I was just joshin' thanks for learning to drive")






