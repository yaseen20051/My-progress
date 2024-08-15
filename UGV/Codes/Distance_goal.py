#!/usr/bin/python3 

from nav_msgs.msg import Odometry

from std_msgs.msg import Float32 ,Int8

from geometry_msgs.msg import Twist

import rospy

import math
class Move():

    def __init__(self) :

        rospy.init_node("Distance_2")

        rospy.Subscriber("/yaw",Float32,self.angle)

        rospy.Subscriber("odom",Odometry,self.orientation)
        rospy.Subscriber("goal_angle",Float32,self.calc_angle)
        rospy.Subscriber("distance_goal",Float32,self.calc_goal)

        self.push = rospy.Publisher("motion",Int8,queue_size=10)
        self.flag_calc = rospy.Publisher("flag",Int8,queue_size=10)
    
        self.theta = 0

        self.x = 0

        self.y = 0 
        
        self.goal_distance = 4.47

        self.goal_Theta = 0

        self.flag = 0
        self.flag_calculation = 0
        self.msg =0

        self.curDis = 0 
        self.imu_get = 0
        self.reached_goals=0
       # constants
        self.rate = 10
        self.imu_out = 100
    def calc_angle(self,msg):
        self.goal_Theta = msg.data

    def calc_goal(self,msg):
        self.goal_distance = msg.data

    def angle(self,msg_angle):
        rospy.logwarn("/////////////////")

          
        self.theta = 360-msg_angle.data
        self.imu_get = 0

    def orientation(self,msg_xy):

        self.x = msg_xy.pose.pose.position.x

        self.y = msg_xy.pose.pose.position.y
        
        self.goal()

    def goal(self):

     self.curDis = math.sqrt((self.x * self.x)+(self.y *self.y))

     if self.flag == 0 :
        if (self.theta >self.goal_Theta-2.5) and  (self.theta <self.goal_Theta+2.5):
            rospy.loginfo('aaaaaaa')
            self.msg = 0 
            self.flag = 1 
            self.flag_calculation = 0
        else :
            self.flag_calculation = 0
            if 0 < self.theta <= 180 :
                if self.theta < self.goal_theta < self.theta + 180 :
                    self.msg = 2
                else :
                    self.msg = 1
            else :
                if self.theta-180 < self.goal_Theta < self.theta :
                    self.msg = 1
                else :
                    self.msg = 2    

     else :
        if self.curDis < self.goal_distance :
           self.msg = 3
           self.flag_calculation = 0
        else :
           self.msg = 0
           self.flag_calculation = 1
     
     self.push.publish(self.msg)
     self.flag_calc.publish(self.flag_calculation)
    def spin(self):

        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            if self.reached_goals != 3:
                if self.imu_get < self.imu_out:

                        self.goal()
                        self.imu_get += 1

            
                else:
                    self.motion = 0
                    self.push.publish(self.motion)
                    rospy.logerr("imu_out")

            rate.sleep()


if __name__=='__main__':
  
     try: 
          pub = Move()
          pub.spin()
          

     except rospy.ROSInterruptException:
          pass
     
    

        

     



