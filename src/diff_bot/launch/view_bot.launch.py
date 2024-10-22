from os import path
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('diff_bot')
    rsp_launch_file = path.join(pkg_share, 'launch', 'rsp.launch.py')
    rsp_launch_description = IncludeLaunchDescription(rsp_launch_file)

    rviz_conf_file = path.join(pkg_share, 'conf', 'view_bot.rviz')
    rviz = Node(package='rviz2', executable='rviz2', output='screen', arguments=['-d', rviz_conf_file])

    jsp_gui = Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui')

    return LaunchDescription([rsp_launch_description, rviz, jsp_gui])
