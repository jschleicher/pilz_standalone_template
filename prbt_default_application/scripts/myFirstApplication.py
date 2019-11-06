#!/usr/bin/env python
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"    # API version
__ROBOT_VELOCITY__ = 0.5          # velocity of the robot

# main program
def start_program():

    rospy.loginfo("Program started") # log

    # important positions
    start_pos = [1.49, -0.54, 1.09, 0.05, 0.91,-1.67]   # joint values
    second_pos = [1.49, -0.5, 1.09, 0.05, 0.91,-1.67]   # joint values


    # move to start point with joint values to avoid random trajectory
    r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))

    rospy.loginfo("Start loop") # log
    while(True):
        # do infinite loop
        r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))
        r.move(Ptp(goal=second_pos, vel_scale=__ROBOT_VELOCITY__))

        # pick the PNOZ

if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')

    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

    # start the main program
    start_program()
