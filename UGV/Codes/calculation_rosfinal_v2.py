#!/usr/bin/python3 
import math
import rospy

from std_msgs.msg import Float32 ,Int8,Float32MultiArray
import os



class calculation():

    def __init__(self) :

        rospy.init_node("calculation")
        rospy.Subscriber("flag",Int8,self.flag)
        rospy.Subscriber("num_goals",Int8,self.num_goals)
        rospy.Subscriber("obstacle",Int8,self.obstacle)
        rospy.Subscriber("coordinates",Float32MultiArray,self.coordinates)

        self.angle = rospy.Publisher("goal_angle",Float32,queue_size=10)
        self.distance = rospy.Publisher("distance_goal",Float32,queue_size=10)
        self.i = 0
        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = 0
        self.x2=0
        self.y2=0
        self.r=0
        self.theta=0
        self.deltax=0
        self.deltay=0
        self.goal_angle=0
        self.goal_distance=0
        self.toggle=1
        self.flag_obs = 0
        self.obstacle_flag = 0

    def flag(self,msg):
        self.toggle = msg.data
    def num_goals(self,msg):
        self.i= msg.data
    def obstacle (self,msg):
        self.obstacle_flag = msg.data
        if self.obstacle_flag == 1:
            self.flag_obs= 1
            self.x1 = self.x
            self.y1 = self.y
        
    def coordinates (self,msg):
        self.x = msg.data[0]
        self.y = msg.data[1]
    def equation(self):


        if (self.toggle  or  self.flag_obs )and self.i != 6 and self.obstacle_flag == 0 :  

            # self.r, self.theta = float(self.points[self.i]) , float(self.points[self.i+1])
            self.y2 = self.r *  math.cos(math.radians(self.theta))
            self.x2 = self.r *  math.sin(math.radians(self.theta))
            self.deltax = self.x2 - self.x1
            self.deltay = self.y2 - self.y1
            self.goal_distance += math.sqrt(self.deltax**2 + self.deltay**2)
            if self.deltax > 0 and self.deltay>0:
                self.goal_angle  = math.degrees(math.atan(abs(self.deltax/self.deltay)))
            elif self.deltax < 0 and self.deltay < 0 :
                self.goal_angle  = 180 + math.degrees(math.atan(abs(self.deltax/self.deltay)))
            elif self.deltax > 0 and self.deltay < 0 :
                self.goal_angle  = 180 - math.degrees(math.atan(abs(self.deltax/self.deltay)))
            else:
                self.goal_angle  = 360- math.degrees(math.atan(abs(self.deltax/self.deltay)))
            self.x1 =  self.x2
            self.y1 =  self.y2 
            self.toggle = 0
            self.flag_obs = 0

        self.angle.publish(self.goal_angle)
        self.distance.publish(self.goal_distance)

    def spin(self):
        

        rate = rospy.Rate(10)
        while not rospy.is_shutdown():    
            if self.i != 4:
                # reading from the distances file
                with open('/home/mohamed/file.txt', 'r') as file:
                   values = file.read()
                   points=values.split()
                #    self.num_of_goals = len(points)/2
                   self.r = float(points[self.i])
                   self.theta = float(points[self.i+1])
            
            else: 
                pass
                  
            self.equation()
            rate.sleep()



if __name__=='__main__':
  
     try: 
          pub = calculation()
          pub.spin()


     except rospy.ROSInterruptException:
          pass
        









        


