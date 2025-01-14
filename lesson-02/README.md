
# Node

* Chạy turtlesim 

```bash
ros2 run turtlesim turtlesim_node 

```

* Các sử dụng  
```bash
ros2 node -h 

```

* Kiểm tra các **node** đang hoạt động 
```bash
ros2 node list

```

* Kiểm tra thông tin của Node 
```bash
ros2 node info /turtlesim

```

# Topic 

* Các sử dụng 

```bash
ros2 topic -h 

```

* Kiểm tra những thông tin **topic** đang hoạt động
```bash
ros2 topic list
```
* Kiểm tra tần số của **topic**
```bash

ros2 topic hz /turtle1/pose

```

* Xem nội dung của **topic** được publish

```bash

ros2 topic echo /turtle1/pose
```
* Publish **topic** bằng command line 

```yaml

ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.1"

```

* Publish **topic** bằng command line 

```yaml

ros2 topic pub -r 10 /turtle1/cmd_vel geometry_msgs/msg/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.1"
```

* Xem kiểu dữ liệu của **topic**

```bash
ros2 topic type /turtle1/cmd_vel
```


# Tạo Message
* Khi tạo **Message** phải tạo trong Packages **Cmake**
* Build pakages msgs

```bash
ros2 pkg create --build-type ament_cmake lesson_02_msgs
```

* Tạo thư mục **msg** nằm trong packages đã tạo src/msg 

    * Tên folder phải đúng là **msg**
    * Tên msgs phải viết hoa chữ cái đầu 

```bash
mkdir msg
```

* Tạo file cấu tạo của msg với tên là **NumData.msg**

```bash
int64 num_01
int64 num_02
```

* Khai báo trong CmakeList.txt

```
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/NumData.msg"

 )
```

* Khai báo trong packages.xml
```
<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>

```

* Tạo packages với **msg** đã tạo trước đó là **NumData**

```bash
string name
NumData num_data
```


# Tạo Node python 

ros2 pkg create --build-type ament_python <package_name>

```bash
ros2 pkg create --build-type ament_python lesson_02_node
```

## Tạo Node Publisher

* Tạo file **turtle_vel_publisher.py** trong **lesson_02_node** folder

```python
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

```


* Cập nhật `setup.py`
Để thêm node Python vào phần `entry_points`, chỉnh sửa file `setup.py` như sau:

```python
entry_points={
    'console_scripts': [
        'turtle_vel_publisher = lesson_02_node.turtle_vel_publisher:main',
    ],
},
```

* Build lại packages 

```bash
colcon build
source install/setup.bash

```

* Chạy Node **turtle_vel_publisher**

```bash
ros2 run lesson_02_node turtle_vel_publisher

```

## Tạo Node Subcriber 

* Tạo file **turtle_vel_subscriber.py** trong **lesson_02_node** folder

```python
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

```


