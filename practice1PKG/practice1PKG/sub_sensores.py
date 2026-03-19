import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32, Int32


class Mysubscriber(Node):

    def __init__(self):
        super().__init__('sensors_listener')
        self.sub_battery = self.create_subscription(
            Int32,
            'robot_battery',
            self.battery_callback,
            10)
        
        self.sub_velocity = self.create_subscription(
            Float32,
            'robot_velocity',
            self.velocity_callback,
            10)
        self.sub_battery  # prevent unused variable warning
        self.sub_velocity  # prevent unused variable warning

    def battery_callback(self, msg):
        # REGLAS DE BATERÍA
        nivel_bat = msg.data
        if nivel_bat < 10:
            self.get_logger().error(f'¡ALERTA!: CRITICAL BATTERY ({nivel_bat}%)')
        elif nivel_bat < 20:
            self.get_logger().warning(f'¡ALERTA!: ALERTA BATERÍA ({nivel_bat}%)')
        else:
            self.get_logger().info(f'Batería normal: {nivel_bat}%')

    def velocity_callback(self, msg):
        velocidad = msg.data
        
        # REGLA DE VELOCIDAD
        if velocidad > 2.0:
            # Usamos warn para que resalte en la consola (amarillo)
            self.get_logger().warning(f'¡ALERTA!: ALERTA VELOCIDAD ({velocidad:.2f} m/s)')
        else:
            self.get_logger().info(f'Velocidad normal: {velocidad:.2f} m/s')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Mysubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()