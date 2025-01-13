# ros2_basic-
## Cài đặt Docker
```
sudo apt install docker.io git python3-pip
pip3 install vcstool
echo export PATH=$HOME/.local/bin:$PATH >> ~/.bashrc
source ~/.bashrc
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
Kiểm tra xem docker đã được cài thành công chưa
```
docker ps
```
## Cài đặt Git
```
sudo apt install git 
```
## Running
### Bước 1:
```
mkdir docker_ws
cd docker_ws
git clone -b hieunm https://github.com/nnhathai/ros2_basic.git
```
### Bước 2:
Cài đặt Extension. Sau đó vào file Dockerfile dùng lệnh "CTRL + SHIFT + P" để tạo Container.
### Bước 3: 
```
xhost +
```
```
docker ps
```
```
docker exec -it <con_name> bash
```
### Bước 4: 
```
apt update
apt install ros-humble-turtlesim
```
### Bước 5: 
```
ros2 run turtlesim turtlesim_node
```
```
ros2 run turtlesim turtle_teleop_key
```