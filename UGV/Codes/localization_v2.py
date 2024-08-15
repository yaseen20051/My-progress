#!/usr/bin/python3

"""
Mind_Cloud
competition : minesweeper
Name        : navigation
Fn          : getting distance from encoders
              pulishe:
                    - distance
              subscribe: 
                    - ticks

Author      : feryal, taha , mona tarek 
Review      : farrag
Date        : 9/4/2023
"""

import rospy
import math
from std_msgs.msg import Int16 , Float32, Int8,Float32MultiArray


class Nav():
    def __init__(self):
        print("enter init")
        #init node
        rospy.init_node('navigation',anonymous=True)
        

        # subscribed topics
        rospy.Subscriber("/back_ticks", Int16, self.enc_callback)        # callback : remove overflow from front ticks 
        rospy.Subscriber("/motion", Int8, self.motion_callback)        # callback : remove overflow from front ticks 
        rospy.Subscriber("/yaw",Float32,self.angle)
        # published topics
        self.pub = rospy.Publisher("/distance", Float32, queue_size = 10)
        self.pub_motion = rospy.Publisher('/system_motion', Int8, queue_size=100)
        self.coord_pub = rospy.Publisher("coordinates",Float32MultiArray,queue_size=10)
        # constants:
        self.enc_out = 100
        self.rate = 10       

        # variables:

        # overflow attributes 
        self.msgsize_min = -32768                       # min size of int 16
        self.msgsize_max = 32768                        # max size of int 16
        self.msgsize_low_wrap = int((self.msgsize_max - self.msgsize_min) * 0.3 + self.msgsize_min  )    #wrap limit @ 0.2 of min range
        self.msgsize_high_wrap = int((self.msgsize_max - self.msgsize_min) * 0.7 + self.msgsize_min  )   #wrap limit @ 0.2 of max range
        
        # encoder
        self.ticks = 0
        self.ticks_prev=0
        self.ticks_mult=0
        self.enc_prev=0

        self.start_rot = 0
        self.end_rot = 0
        self.rot = 0
        self.prev_rot = 0
        self.acc_rots = False
        self.relative_x = 0 
        self_relative_y = 0
        self.coordinates = Float32MultiArray()
        self.x=0
        self.y = 0



        # sensors
        self.enc_get = 0
        self.theta = 0
        # distance calculation attributes
        self.diameter = rospy.get_param("diameter", 0.24)                            # in meter
        self.no_of_ticks_per_rev = rospy.get_param("no_of_ticks_per_rev", 580)

        self.distance = 0.0
        self.final_distance = 0
        self.motion = 0
 
    def angle(self,msg_angle):
       
        self.theta =360- msg_angle.data

    def motion_callback(self, msg):                              
        self.motion = msg.data        

    def enc_callback(self, enc_msg): 

        if self.motion == 1 or self.motion == 2:
            self.end_rot = enc_msg.data + (self.ticks_mult * (self.msgsize_max - self.msgsize_min)) 
            self.rot = (self.end_rot - self.start_rot)  + self.prev_rot
                  
        else:                    
            self.start_rot = enc_msg.data + (self.ticks_mult * (self.msgsize_max - self.msgsize_min)) 
            self.prev_rot = self.rot    

        self.enc_get = 0
        # high overflow (from + to -)
        if (enc_msg.data < self.msgsize_low_wrap and self.enc_prev > self.msgsize_high_wrap) :             
            self.ticks_mult = self.ticks_mult + 1

        # low overflow (from - to +)
        if (enc_msg.data > self.msgsize_high_wrap and self.enc_prev < self.msgsize_low_wrap) :             
            self.ticks_mult = self.ticks_mult - 1
           
        # self.ticks = 1.0 * (self.enc + (self.ticks_mult * (self.msgsize_max - self.msgsize_min))) 
        self.enc_prev = enc_msg.data                                   #update enc reading (with overflow) (used in calc)
        self.ticks = (enc_msg.data  + (self.ticks_mult * (self.msgsize_max - self.msgsize_min))) - self.rot  

    def localization(self,ticks):    
        #distance                     
        self.distance = (math.pi*self.diameter*ticks)/self.no_of_ticks_per_rev

        if self.motion == 1 or self.motion == 2:
            self.x += self.relative_x
            self.y += self.relative_y

            self.distance_prev = self.distance
        
        self.relative_x = (self.distance-self.distance_prev ) * math.sin(math.radians(self.angle))
        self.relative_y = (self.distance-self.distance_prev ) * math.cos(math.radians(self.angle))

        self.coordinates.data = [self.x + self.relative_x , self.y+ self.relative_y]
    

        self.coord_pub.publish (self.coordinates)
        self.pub.publish(self.distance)

    def run(self):
        rate=rospy.Rate(self.rate)
        while not rospy.is_shutdown():    
            
            if self.enc_get < self.enc_out:

                self.localization(self.ticks)
                self.enc_get+=1
        
            else:
                self.motion = 0
                self.pub_motion.publish(self.motion)
                rospy.logwarn("encoder_out")

            rate.sleep()

# main function.    
if __name__ == '__main__':                      #code start here
    NavToGUI = Nav()
    try:
        NavToGUI.run()
    except rospy.ROSInterruptException: 
        pass