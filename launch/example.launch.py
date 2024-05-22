import launch
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    config = os.path.join(get_package_share_directory('diagnostic_example'), 'config.yaml')

    aggregator = Node(
        package='diagnostic_aggregator',
        executable='aggregator_node',
        output='screen',
        parameters=[config])
    temperature_talker = Node(
            package='diagnostic_example',
            executable='temperature_talker')
    humidity_talker = Node(
            package='diagnostic_example',
            executable='humidity_talker')
    status_talker = Node(
            package='diagnostic_example',
            executable='status_talker')
            
    return launch.LaunchDescription([
        aggregator,
        temperature_talker,
        humidity_talker,
        status_talker,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=aggregator,
                on_exit=[launch.actions.EmitEvent(
                    event=launch.events.Shutdown())],
            )),
    ])
