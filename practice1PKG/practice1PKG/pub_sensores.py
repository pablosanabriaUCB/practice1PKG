import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import String, Float32, Int32


class MyPublisher(Node):

    def __init__(self):
        super().__init__('robot_sensors')
        self.pub_battery = self.create_publisher(Int32, 'robot_battery', 10)
        self.pub_velocity = self.create_publisher(Float32, 'robot_velocity', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg_bat = Int32()
        msg_bat.data = random.randint(0, 100)
        self.pub_battery.publish(msg_bat)

        msg_float = Float32()
        msg_float.data = random.uniform(0.0, 2.5)
        self.pub_velocity.publish(msg_float)

        self.get_logger().info(f'Publicando Batería: {msg_bat.data} y Vel: {msg_float.data}m/s')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MyPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()