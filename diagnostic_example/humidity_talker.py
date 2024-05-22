import rclpy
from rclpy.node import Node
from diagnostic_updater import Updater, DiagnosticStatusWrapper
import random

class HumidityNode(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.updater = Updater(self)
        self.updater.setHardwareID("Humidity Sensor")
        
        self.updater.add("Humidity Sensor", self.check_humidity)
        self.timer = self.create_timer(5, self.updater.update)

    def check_humidity(self, stat):
        humidity = 50 + random.randint(-15, 15)
        stat.add("Humidity", f"{humidity}%")
        
        if humidity < 40:
            stat.summary(DiagnosticStatusWrapper.WARN, "Humidity is too low")
            self.get_logger().warn(f'Humidity is: {humidity}')
        elif humidity > 60:
            stat.summary(DiagnosticStatusWrapper.WARN, "Humidity is too high")
            self.get_logger().warn(f'Humidity is: {humidity}')
        else:
            stat.summary(DiagnosticStatusWrapper.OK, "Humidity is normal")
            self.get_logger().info(f'Humidity is: {humidity}')
        
        return stat

def main(args=None):
    rclpy.init(args=args)
    node = HumidityNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
