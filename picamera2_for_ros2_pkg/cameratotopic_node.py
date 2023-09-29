#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from picamera2 import Picamera2
from cv_bridge import CvBridge


class ImagePublisher(Node):

    def __init__(self):
        super().__init__("image_publisher")
        self.pub = self.create_publisher(Image, "/image", 10)
        timer_period = 0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bridge = CvBridge()
        self.cap = Picamera2()
        video_config = self.cap.create_video_configuration(main={"size": (426, 240), "format": "RGB888"}) # change as needed
        self.cap.configure(video_config)
        self.cap.start()

    def timer_callback(self):
        img=self.cap.capture_array()
        
        # scale_percent = 50 # scale image to 50% of original size
        # width = int(img.shape[1] * scale_percent / 100)
        # height = int(img.shape[0] * scale_percent / 100)
        # dim = (width, height)
        # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        self.pub.publish(self.bridge.cv2_to_imgmsg(img, "rgb8"))
        self.get_logger().info('Publishing...')

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()