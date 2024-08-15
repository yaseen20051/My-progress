#!/usr/bin/python3 

from nav_msgs.msg import Odometry

from std_msgs.msg import Float32

from geometry_msgs.msg import Twist

import rospy

import math
class Move():

    def __init__(self) :

        rospy.init_node("Distance_2")

        rospy.Subscriber("euler",Float32,self.angle)

        rospy.Subscriber("odom",Odometry,self.orientation)

        self.push = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        
        self.theta = 0

        self.x = 0

        self.y = 0 
        
        self.goal_distance = 5

        self.goal_Theta = 120 

        self.flag = 0

        self.msg = Twist()

        self.curDis = 0 
        
    def angle(self,msg_angle):

          
        self.theta = msg_angle.data

    def orientation(self,msg_xy):

        self.x = msg_xy.pose.pose.position.x

        self.y = msg_xy.pose.pose.position.y
        
        self.goal()

    def goal(self):

     self.curDis = math.sqrt((self.x * self.x)+(self.y *self.y))

     if self.flag == 0 :
        if round(self.theta) != round(self.goal_Theta) :
            self.msg.angular.z = 0.7 
        else :
            self.flag = 1 
            self.msg.angular.z = 0 
     else :
        if self.curDis < self.goal_distance :
           self.msg.linear.x = 0.7 
        else :
           self.msg.linear.x = 0
     
     self.push.publish(self.msg)


if __name__=='__main__':
  
     try: 
          pub = Move()
         
          rospy.spin()

     except rospy.ROSInterruptException:
          pass
     
    

        

     



