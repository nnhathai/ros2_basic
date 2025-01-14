import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleVelPublisher(Node):
    def __init__(self):
        super().__init__('turtle_vel_publisher')
        # Tạo publisher cho topic '/turtle1/cmd_vel'
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_velocity)  # Tạo timer (2Hz)
        self.get_logger().info("Turtle Velocity Publisher Node has started.")

    def publish_velocity(self):
        # Tạo một message Twist
        msg = Twist()
        msg.linear.x = 1.0  # Vận tốc tuyến tính (m/s)
        msg.angular.z = 0.5  # Vận tốc góc (rad/s)

        # Publish message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)  # Khởi tạo rclpy
    node = TurtleVelPublisher()  # Tạo node
    try:
        rclpy.spin(node)  # Giữ cho node hoạt động
    except KeyboardInterrupt:
        node.get_logger().info("Node stopped by user.")
    finally:
        node.destroy_node()  # Hủy node
        rclpy.shutdown()  # Tắt rclpy


if __name__ == '__main__':
    main()
