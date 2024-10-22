from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('diff_bot')
    urdf_filename = LaunchConfiguration('urdf_filename')
    urdf_filename_arg = DeclareLaunchArgument('urdf_filename', default_value='bot.urdf.xml', description='urdf file to load')
    urdf_file = PathJoinSubstitution([pkg_share, 'urdf', urdf_filename])
    urd = Command(['xacro ', urdf_file])
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='false', description='Sync with sim time if true')
    params={'robot_description': urd, 'use_sim_time': use_sim_time, 'publish_rate': '50.0'}
    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen', parameters=[params])
    return LaunchDescription([urdf_filename_arg, use_sim_time_arg, rsp])
