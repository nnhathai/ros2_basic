import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleVelSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_vel_subscriber')
        # Tạo subscriber cho topic '/turtle1/cmd_vel'
        self.subscription = self.create_subscription(
            Twist,                # Loại message
            '/turtle1/cmd_vel',   # Tên topic
            self.listener_callback,  # Hàm callback xử lý dữ liệu nhận được
            10                    # Độ dài hàng đợi (queue size)
        )
        self.get_logger().info("Turtle Velocity Subscriber Node has started.")

    def listener_callback(self, msg):
        # Hàm callback xử lý message nhận được
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        print("Linear x : ", linear_x)
        print("angular z : ", angular_z)


def main(args=None):
    rclpy.init(args=args)  
    node = TurtleVelSubscriber() 
    try:
        rclpy.spin(node)  # Giữ cho node hoạt động
    except KeyboardInterrupt:
        node.get_logger().info("Node stopped by user.")
    finally:
        node.destroy_node()  
        rclpy.shutdown()  


if __name__ == '__main__':
    main()
