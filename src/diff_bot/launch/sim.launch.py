from os import path
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('diff_bot')
    urdf_filename = 'gazebo_sim.xml'
    rsp_launch_file = path.join(pkg_share, 'launch', 'rsp.launch.py')
    rsp_launch_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([rsp_launch_file]),
        launch_arguments={'urdf_filename': urdf_filename}.items())

    #gz
    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')
    gz_sim_launch_file = path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument('world', default_value='empty.world', description='world to load')
    world_file = PathJoinSubstitution([pkg_share, 'worlds', world])
    gz_sim_launch_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([gz_sim_launch_file]),
        launch_arguments={'gz_args': ['-r -v4 ', world_file], 'on_exit_shutdown': 'true'}.items())

    # spawn robot
    create_bot = Node(package='ros_gz_sim', executable='create',
        arguments=['-topic', 'robot_description', '-name', 'diff_bot', '-z', '0.1'])

    # bridge
    bridge_params = {'config_file': path.join(pkg_share, 'conf', 'ros_gz_bridge.yaml')}
    ros_gz_bridge = Node(package='ros_gz_bridge', executable='parameter_bridge', parameters=[bridge_params])
    
    return LaunchDescription([world_arg, rsp_launch_description, gz_sim_launch_description, create_bot, ros_gz_bridge])
