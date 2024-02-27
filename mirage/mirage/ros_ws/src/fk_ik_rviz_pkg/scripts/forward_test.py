import compas_fab
from compas.robots import Configuration
from compas_fab.backends import PyBulletClient
import pathlib
import time

with PyBulletClient() as client:
    # TODO: Change hardcoded Python file
    file_path = pathlib.Path(__file__).parent.resolve()
    urdf_filename = compas_fab.get('../../../../../../cross_embodiment_test_ws/src/fk_ik_rviz_pkg/scripts/ur5e.urdf')
    robot = client.load_robot(urdf_filename)

    configuration = Configuration.from_revolute_values([0,0,0,0,0,0,0])

    frame_WCF = robot.forward_kinematics(configuration)

    # Given 4x4 matrix, it is 4th column (position), first column, and then second column
    print("Frame in the world coordinate system")
    print(frame_WCF)
