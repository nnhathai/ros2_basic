FROM osrf/ros:humble-desktop-full


# Update package index and install Python 3
RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN apt-get install -y nano
RUN apt-get install -y net-tools
RUN apt-get install -y git

RUN echo "export ROS_DOMAIN_ID=15" >> ~/.bashrc
RUN echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bashrc

RUN echo "alias nb='nano ~/.bashrc'" >> ~/.bashrc
RUN echo "alias sb='source ~/.bashrc'" >> ~/.bashrc
RUN echo "alias ws='cd /workspaces/ros2_training/ros2_ws'" >> ~/.bashrc

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /workspaces/ros2_training/ros2_ws/install/setup.bash" >> ~/.bashrc