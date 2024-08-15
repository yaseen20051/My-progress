#!/usr/bin/python3 
import math
import rospy

from std_msgs.msg import Float32 ,Int8



class calculation():

    def __init__(self) :

        rospy.init_node("calculation")
        rospy.Subscriber("flag",Int8,self.flag)
        self.angle = rospy.Publisher("goal_angle",Float32,queue_size=10)
        self.distance = rospy.Publisher("distance_goal",Float32,queue_size=10)

        with open('/home/mohamed/file.txt', 'r') as file:
            self.values = file.read()
            self.points=self.values.split()
        
        self.i = 0
        self.x1 = 0
        self.y1 = 0
    def flag(self,msg):
        self.points()
        self.toggle = msg.data
        if self.toggle == 1:
            self.i = self.i + 2

    def points(self):
        if self.toggle == 1 and self.i != 6:
            self.r, self.theta = int(self.points[self.i]) , int(self.points[self.i+1])
            self.y2 = self.r *  math.cos(math.radians(self.theta))
            self.x2 = self.r *  math.sin(math.radians(self.theta))
            self.deltax = self.x2 - self.x1
            self.deltay = self.y2 - self.y1
            self.distance = math.sqrt(self.deltax**2 + self.deltay**2)
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

        self.angle.publish(self.goal_angle)
        self.distance.publish(self.distance)


if __name__=='__main__':
  
     try: 
          pub = calculation()
          rospy.spin()


     except rospy.ROSInterruptException:
          pass
        









        


