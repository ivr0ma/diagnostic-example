import rclpy
from rclpy.node import Node
from diagnostic_updater import Updater, DiagnosticStatusWrapper
import random

class TemperatureNode(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.updater = Updater(self)
        self.updater.setHardwareID("Temperature Sensor")
        
        self.updater.add("Temperature Sensor", self.check_temperature)
        self.timer = self.create_timer(5, self.updater.update)

    def check_temperature(self, stat):
        temperature = 20 + random.randint(-5, 5)  # Симулируем изменение температуры
        stat.add("Temperature", f"{temperature} °C")
        
        if temperature < 18:
            stat.summary(DiagnosticStatusWrapper.WARN, "Temperature is too low")
            self.get_logger().warn(f'Temperature is: {temperature}')
        elif temperature > 25:
            stat.summary(DiagnosticStatusWrapper.WARN, "Temperature is too high")
            self.get_logger().warn(f'Temperature is: {temperature}')
        else:
            stat.summary(DiagnosticStatusWrapper.OK, "Temperature is normal")
            self.get_logger().info(f'Temperature is: {temperature}')
        
        return stat

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
