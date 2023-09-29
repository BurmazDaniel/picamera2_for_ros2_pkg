# picamera2_for_ros2_pkg

This just a simple publisher node that extracts camera data from Raspberry Pi 4's csi port and gets published intro a ROS2 topic. As of the time of writing Imx219, Imx477(High Quality Camera) or Imx708(Camera module 3) sensors do not work as expected on Ubuntu 22.04 because of missing Libcamera and Picamera2 libraries, outdated linux kernel and mismatch of python version. All these problems can be avoided by using the lates **Raspberry Pi OS 64 bit(Debian Bullseye)**.

## Installation  
1. ROS2 Humble Hawksbill. You can compile it from source or use [this build](https://github.com/Ar-Ray-code/rpi-bullseye-ros2) for **Raspberry Pi OS 64 bit(Debian Bullseye)**. Kudos to [Ar-Ray](https://github.com/Ar-Ray-code).

2. A working camera. Don't forget to write specific dtoverlay for your camera in `/boot/config.txt`. See [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/camera_software.html). You can test your camera using `libcamera-hello`.

3. Colcon. Build your packages. Install with `pip install colcon-ros`. It should install colcon-common-extensions and many others.

4. ROS Cv-Bridge. Converts from Picamera2 camera capture array to ROS messages. Install with `sudo apt-get install python3-cv-bridge`<br><br>

Create a ROS2 workspace using `mkdir -p ~/ros2_ws/src` then `cd ~/ros2_ws/src` and clone my package in this directory.<br>

Use `colcon build` to build the package then `source install/setup.bash`.<br>

Lastly type `ros2 run picamera2_for_ros2_pkg cameratotopic_node` to start the node.<br><br>

Check your topic with `ros2 topic echo /image`.

## Known issues
This is not the best implementation for publishing images using your Raspberry Pi. A C++ version would be much better.

![Code Profilling](https://i.imgur.com/9EpRxKa.png)

Unfortunately converting a camera capture array to a ROS message kills the poor little pi 4's cpu at high resolutions. I personally get around 15 fps at 426x240.

## Why?

I was working for my bachelor's thesis and this was the only solution for me. Picamera2 library is dependent on libcamera and I don't think we will see these two fully supported in Ubuntu any time soon.<br>

Any advice is much appreciated.



