"Debug Script for Picar-X"
from picarx_improved import Picarx
from picarx_improved import Grayscale_Module
# try:
#     from robot_hat import *
#     from robot_hat import reset_mcu
#     reset_mcu()
#     time.sleep(0.01)
# except ImportError:
#     print("This computer does not appear to be a PiCar-X system (robot_hat is not present). Shadowing hardware calls with substitute functions")
#     from sim_robot_hat import *
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import statistics as st
import logging
import numpy as np
import concurrent.futures
from readerwriterlock import rwlock


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

class GreyScale_Sensing(object):
    def __init__(self, input_pins = ['A0', 'A1', 'A2']):
        pin1, pin2, pin3 = input_pins
        self.grayscale_sensor = Grayscale_Module(pin1, pin2, pin3, ref = 1000)
    
    def list_grayscale_data(self):
        #placeholder
        self.grayscale_data = self.grayscale_sensor.get_grayscale_data()
        return self.grayscale_data
    
    def producer(self, sensor_bus, timing):
        while True:
            #information being sent
            message = self.grayscale_data
            #sending the information
            sensor_bus.write(message)
            #take a break
            time.sleep(timing)

        

class GreyScale_Interpret(object):
    def __init__(self):
        self.window_size  = 10

        self.left_channel = []
        self.center_channel = []
        self.right_channel = []

    def get_line_status(self, sensor_data):
        #fills channel lists
        self.left_channel.append(int(sensor_data[0]))
        self.center_channel.append(int(sensor_data[1]))
        self.right_channel.append(int(sensor_data[2]))

        #Only look at a window of ten data points per channel. Move by one as data filters by deleting index 0
        if len(self.left_channel) > self.window_size:
            self.left_channel.pop(0)
            self.center_channel.pop(0)
            self.right_channel.pop(0)
        
        # averages of the windows of 10
        avg1 = int(st.mean(self.left_channel))
        avg2 = int(st.mean(self.center_channel))
        avg3 = int(st.mean(self.right_channel))

        avgs = [avg1, avg2, avg3]

        #use min and max values of the means instead of channles to limit error due to different light conditions
        minimum = min(avgs)
        maximum = max(avgs)
        rang = maximum - minimum

        avg_a1 = (avg1 - minimum) / rang
        avg_a2 = (avg2 - minimum) / rang
        avg_a3 = (avg3 - minimum) / rang

        steer_angle = (avg_a3 - avg_a1) / (avg_a1 + avg_a2 + avg_a3)
        
        return steer_angle
    
    def consumer_producer(self, sensor_bus, interpretor_bus, timing):
        while True:
            #what is being read from the producer
            message = sensor_bus.read()
            #take message and interpret data
            steer_angle = self.get_line_status(message)
            #write the interpreted data to the bus
            interpretor_bus.write(steer_angle)
            #take a break
            time.sleep(timing)

class Controller(object):
    def __init__(self, k_control = 25):
        self.k_control = k_control
        self.chad = Picarx()
    def follow_line(self, steer_angle):
        follow = self.k_control * steer_angle
        return follow
    def consumer(self, interpretor_bus, timing):
        while True:
            #read the message sent from previous bus
            message = interpretor_bus.read()
            #actuate
            follow = self.follow_line(message)
            self.chad.set_dir_servo_angle(follow)
            #take a break
            time.sleep(timing)


    
class Camera_Module():
    def __init__(self):
        self.color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}  #Here is the range of H in the HSV color space represented by the color
        self.kernel_5 = np.ones((5,5),np.uint8) #Define a 5×5 convolution kernel with element values of all 1.
        self.center_line = 0
        self.center_screen = 160/2 #from window resize

    def color_detect(self,img,color_name):

        # The blue range will be different under different lighting conditions and can be adjusted flexibly.  H: chroma, S: saturation v: lightness
        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # In order to reduce the amount of calculation, the size of the picture is reduced to (160,120)
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # Convert from BGR to HSV
        color_type = color_name
    
        mask = cv2.inRange(hsv,np.array([min(self.color_dict[color_type]), 60, 60]), np.array([max(self.color_dict[color_type]), 255, 255]) )           # inRange()：Make the ones between lower/upper white, and the rest black
        if color_type == 'red':
            mask_2 = cv2.inRange(hsv, (self.color_dict['red_2'][0],0,0), (self.color_dict['red_2'][1],255,255)) 
            mask = cv2.bitwise_or(mask, mask_2)

        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel_5,iterations=1)              # Perform an open operation on the image 

        # Find the contour in morphologyEx_img, and the contours are arranged according to the area from small to large.
        _tuple = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)      
        # compatible with opencv3.x and openc4.x
        if len(_tuple) == 3:
            _, contours, hierarchy = _tuple
        else:
            contours, hierarchy = _tuple
    
        color_area_num = len(contours) # Count the number of contours

        if color_area_num > 0: 
            for i in contours:    # Traverse all contours
                x,y,w,h = cv2.boundingRect(i)      # Decompose the contour into the coordinates of the upper left corner and the width and height of the recognition object

                self.center_line = x + w/2 #Define the center of the line the middle line between the min and max of the blue rectangles

                # Draw a rectangle on the image (picture, upper left corner coordinate, lower right corner coordinate, color, line width)
                if w >= 8 and h >= 8: # Because the picture is reduced to a quarter of the original size, if you want to draw a rectangle on the original picture to circle the target, you have to multiply x, y, w, h by 4.
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Draw a rectangular frame
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# Add character description

        return img,mask,morphologyEx_img
    
    def frame_of_interest(self, central_line):
        return (central_line - self.center_screen)/self.center_screen
    
class CarBus():
    def __init__(self):
        self.message = 0
        self.lock = rwlock.RWLockWriteD()
    
    def write(self, message):
        with self.lock.gen_wlock():
            self.message = message

    def read(self):
        with self.lock.gen_rlock():
            message = self.message
            


         
    

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

def week_3a():
    chad = Picarx()
    man = Manuevering()
    interpretation = GreyScale_Sensing()
    move = GreyScale_Moving()

    clock = 0
    start_clock = time.time()



    while clock < 7:
        greyscale_data = chad.get_grayscale_data()

        steer_angle = interpretation.get_line_status(greyscale_data)
        follow = move.follow_line(steer_angle)

        chad.set_dir_servo_angle(follow)
        chad.forward(1)

        clock = time.time() - start_clock

def week_3b():
    chad = Picarx()
    move = Controller()
    cam = Camera_Module()

    with PiCamera() as camera:
        print("start color detect")
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)

        start_clock = time.time()

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
            img = frame.array
            img,img_2,img_3 =  cam.color_detect(img,'blue')  # Color detection function
            cv2.imshow("video", img)    # OpenCV image show
            cv2.imshow("mask", img_2)    # OpenCV image show
            cv2.imshow("morphologyEx_img", img_3)    # OpenCV image show
            rawCapture.truncate(0)   # Release cache
            #take the line and have the car steer accordingly
            center_line = cam.frame_of_interest(cam.center_line)
            follow = move.follow_line(center_line)
            chad.set_dir_servo_angle(follow)
            chad.forward(1)
            
            #clock time
            if (time.time() - start_clock) >= 7:
                break
        
        print('quit ...')
        cv2.destroyAllWindows()
        camera.close()

def week4():
    #Defining the modules used
    sensor = GreyScale_Sensing()
    interpreter = GreyScale_Interpret()
    controller = Controller()

    #Defining the buses
    sensor_bus = CarBus()
    interpreter_bus = CarBus()

    #timing
    producer_delay = 0.01
    cons_prod_delay = 0.01
    consumer_delay = 0.01

    with concurrent.futures.ThreadPoolExecutor(max_workers =2) as executor:
        eSensor = executor.submit(sensor.producer , sensor_bus , producer_delay)
        eInterpreter = executor.submit(interpreter.consumer_producer , sensor_bus , interpreter_bus , cons_prod_delay)
        eController = executor.submit(controller.consumer, interpreter_bus, consumer_delay)

    eSensor.result()
    eInterpreter.result()
    eController.result()

    

            

if __name__ == "__main__":
    chad = Picarx()
    week4()
        




        






