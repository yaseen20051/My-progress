#!/usr/bin/python3 
"""
Mind_Cloud
competition : UGVC
Name        : navigation
Fn          : calculating goal distance and angle 
              relatve to the rover's position
              *note: this code considers that angles are
                    given in the cw direction from the north
              pulishe:
                    - motion
                    - flag_calculation
              subscribe: 
                    - distance
                    - yaw
              reades from:
                    - file.txt
                
                    

Author      : Salma Hamdy , Yaseen Islam , Nourhan Ali , Mohamed Naguib  
"""

from nav_msgs.msg import Odometry

from std_msgs.msg import Float32 ,Int8

from geometry_msgs.msg import Twist

import rospy

import math
class Move():

    def __init__(self) :

        rospy.init_node("Distance_2")


        #topics 

        rospy.Subscriber("/yaw",Float32,self.angle)

        rospy.Subscriber("distance",Float32,self.orientation)
        rospy.Subscriber("goal_angle",Float32,self.calc_angle)
        rospy.Subscriber("distance_goal",Float32,self.calc_goal)
        rospy.Subscriber("obstacle",Int8,self.obstacle)

        self.push = rospy.Publisher("motion",Int8,queue_size=10)
        self.flag_calc = rospy.Publisher("flag",Int8,queue_size=10)
        self.num_goals= rospy.Publisher("num_goals",Int8,queue_size=10)
      # initialize variables 
        
        self.theta = 0
        self.goal_Theta = None
        self.goal_distance = None
        self.flag = 0
        self.flag_calculation = 0
        self.msg =0
        self.last_goal=0
        self.curDis = 0 
        self.imu_get = 0
        self.reached_goals=0
        self.rover_head= None
        

       # constants
        self.rate = 10
        self.imu_out = 100
    def calc_angle(self,msg):
        self.goal_Theta = msg.data
        
      

    def calc_goal(self,msg):
        self.goal_distance = msg.data
        
        

    def angle(self,msg_angle):
       

          
        self.theta =360- msg_angle.data
        self.imu_get = 0

        if self.rover_head == None:
            self.rover_head = self.theta
        

    def obstacle(self,msg):

        self.obs_flag = msg.data

        if self.obs_flag == 1 :
            self.goal_Theta = None
            self.goal_distance = None
            self.rover_head = self.theta



    def orientation(self,msg_xy):
        
        self.curDis=abs(msg_xy.data)
         
        self.goal()
     
    def goal(self):
     '''
       this function move the rover to it's goal points 
       we should make (self.flag_calculation=0) in most of times to just calculate one time every point
       we just checked that the last_goal != self.goal_distance and that's because the rover rotate while moving forward
       to make the angle right so we use the first condition to make it calculate agaion 

      / motion guide :
       3---> forward
       2 ---> left
       1---> right
       0 --> backward
        
     '''
     minmum = self.goal_Theta-1.5
     maximum = self.goal_Theta+1.5
     
     if self.goal_Theta < 1.5 :
         minmum = 0
     elif self.goal_Theta > 358.5:
         maximum = 360
    

     if self.goal_distance == self.last_goal and self.reached_goals!=6 : 
                                               
         self.flag_calculation=1

     if self.flag == 0 and  (self.goal_Theta != None) and (self.reached_goals!=6): 
                                                                            
        if self.flag_calculation:
            self.flag_calculation=0
        
        if (self.theta > minmum) and (self.theta < maximum): # here it reached it's angle
            self.msg=0
            self.flag = 1 
            self.flag_calculation = 0
           
        else :
            '''
            this conditions to rotate the rover to nearest way 
            '''
            if (0 < self.rover_head) and  (self.rover_head<= 180) : 
                if (self.rover_head < self.goal_Theta) and (self.goal_Theta< self.rover_head+ 180) :
                    self.msg=1
                    self.flag_calculation = 0
                else :
                     self.msg=2
                     self.flag_calculation = 0
            else :
                if (self.rover_head-180 < self.goal_Theta)and (self.goal_Theta < self.rover_head) :
                   self.msg=2
                   self.flag_calculation = 0
                else :
                   self.msg=1
                   self.flag_calculation = 0
    
     elif (self.flag==1) and (self.goal_distance != None)  and (self.reached_goals!=6) and (self.goal_distance != self.last_goal):

        if (self.theta >self.goal_Theta-3) and (self.theta <self.goal_Theta+3):

            if self.curDis < self.goal_distance +0.15 and  self.curDis > self.goal_distance -0.15: #here  raeched the point
                self.msg=0
                self.flag_calculation = 1
                self.reached_goals+=2
                self.flag=0
                self.last_goal=self.goal_distance
                rospy.logerr(self.reached_goals)
                
            
            
            else :
                self.msg=3
                self.rover_head=self.theta
                self.flag_calculation = 0
        else:
            self.flag=0
     
     self.push.publish(self.msg)
     self.flag_calc.publish(self.flag_calculation)
     self.num_goals.publish(self.reached_goals)
    def spin(self):

        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            if self.reached_goals != 2:
                if self.imu_get < self.imu_out:

                        self.goal()
                        self.imu_get += 1

            
                else:
                    self.motion = 0
                    self.push.publish(self.motion)
                    rospy.logerr("imu_out")
            else:
                rospy.logwarn("ALL POINTS REACHED !!!!")
            rate.sleep()


if __name__=='__main__': # the code starts here 
  
     try: 
          pub = Move() 
          pub.spin()
          

     except rospy.ROSInterruptException:
          pass
     
    

        

     



