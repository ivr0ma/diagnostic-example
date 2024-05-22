import rclpy
from rclpy.node import Node
from diagnostic_updater import Updater, DiagnosticStatusWrapper
import random

class StatusNode(Node):
    def __init__(self):
        super().__init__('status_node')
        self.updater = Updater(self)
        self.updater.setHardwareID("Status")
        
        self.updater.add("Robot Status", self.check_temperature)
        self.timer = self.create_timer(5, self.updater.update)

    def check_temperature(self, stat):
        battery_charge = random.randint(1, 100)
        param_1 = random.randint(-10, 10)
        stat.add("Battery charge", f"{battery_charge}")
        stat.add("Param 1", f"{param_1}")
        
        if battery_charge < 18:
            stat.summary(DiagnosticStatusWrapper.WARN, "Battery charge is too low")
            self.get_logger().warn(f'Battery charge is: {battery_charge}')
        else:
            stat.summary(DiagnosticStatusWrapper.OK, "Battery charge is normal")
            self.get_logger().info(f'BaTemperaturettery charge is: {battery_charge}')
        
        return stat

def main(args=None):
    rclpy.init(args=args)
    node = StatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
