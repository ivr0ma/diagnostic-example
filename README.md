# Diagnostics Example

Этот репозиторий демонстрирует возможности диагностики ROS с использованием [пакета ROS diagnostics](https://github.com/ros/diagnostics). Он включает примеры узлов, которые симулируют поведение сенсоров, а также узлы, отображающие состояние робота, в дополнение к агрегаторному узлу, который группирует диагностические сообщения в категории "сенсоры" и "основное".

## Зависимости

Убедитесь, что установлены следующие зависимости:
- ROS 2 
- diagnostic_updater
- diagnostic_aggregator
- rqt_runtime_monitor
- rqt_robot_monitor

```bash
sudo apt update
sudo apt install ros-humble-diagnostic-updater ros-humble-diagnostic-msgs ros-humble-diagnostic-aggregator ros-humble-rqt-runtime-monitor ros-humble-rqt-robot-monitor
```

## Установка

1. Клонируйте репозиторий в локальное рабочее пространство ROS 2:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ros3_ws/src
   git clone git@github.com:ivr0ma/diagnostic-example.git
   ```
2. Перейдите в своё рабочее пространство и соберите пакет:
   ```bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ```

## Запуск

Для запуска примера используйте следующую команду:
```bash
ros2 launch diagnostic_example example.launch.py
```

Это запустит агрегаторный узел вместе с узлами симуляции сенсоров (`temperature_talker`, `humidity_talker`, `status_talker`). Агрегатор будет группировать и отображать диагностическую информацию, категоризированную под "Sensors" и "Main".

В другом терминале:
```bash
ros2 run rqt_robot_monitor rqt_robot_monitor
```
