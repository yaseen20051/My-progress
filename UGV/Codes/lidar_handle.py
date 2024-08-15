#!/usr/bin/python3 
import rospy
from std_msgs.msg import Float32MultiArray,Float32,Int8

class lidar_decesion():
    def __init__(self):
        rospy.init_node("obstcale_handle")

        rospy.Subscriber("lidar_readings",Float32MultiArray,self.reading)

        rospy.Subscriber("distance",Float32,self.distance)

        self.obstcale_ind = rospy.Publisher("obstacle",Int8,queue_size=10)

        self.motion_pub = rospy.Publisher("motion",Int8,queue_size=10)

        self.forward = 0
        self.right =0 
        self.left =0 
        self.obstcale = 0
        self.motion = 0
        self.goalDist = 2
        self.add_distance= 0
        self.prev_distance=0
        

    def reading(self,msg):
        self.forward = msg.data[0]
        self.right = msg.data[1]
        self.left = msg.data[2]


    def distance(self,msg):
          self.add_distance = msg.data
          if(self.obstcale == 1):
                self.prev_distance = msg.data
          

    def decesion(self):
        if(self.forward <= 2):
                
                self.obstcale = 1
                if(self.right>self.left):
                        self.motion = 1
                elif (self.right<self.left):
                        self.motion = 2
                else:
                      self.motion = 1
        else :
              
              if(self.add_distance < self.prev_distance+2.5) and (self.add_distance > (self.prev_distance+2)):
                    self.obstcale = 0
                    self.motion = 0
              else:
                    self.motion = 3

        self.obstcale_ind.publish(self.obstcale)
        self.motion_pub.publish(self.motion)

if __name__=='__main__': # the code starts here 
  
     try: 
          pub = lidar_decesion() 
          while(not rospy.is_shutdown()):
                pub.reading()
                
          

     except rospy.ROSInterruptException:
          pass
        
              
              


    
                

