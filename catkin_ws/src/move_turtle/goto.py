
#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def goto_point(x, y):
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.orientation.w = 0.1114392120325298

    pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
    rospy.init_node("goto_node", anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        pub.publish(goal)
        rate.sleep()

if _name_ == '_main_':
    try:
        goto_point(7.5330729484558105, -2.577113628387451)  # Utilisez les coordonnées de votre premier point ici
    except rospy.ROSInterruptException:
        pass
