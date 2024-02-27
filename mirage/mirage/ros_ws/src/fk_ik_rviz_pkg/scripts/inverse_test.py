import compas_fab
from compas.geometry import Frame
from compas_fab.backends import PyBulletClient

with PyBulletClient() as client:
    urdf_filename = compas_fab.get('../../../../../../cross_embodiment_test_ws/src/fk_ik_rviz_pkg/scripts/panda.urdf')
    robot = client.load_robot(urdf_filename)

    # Given 4x4 matrix, it is 4th column (position), first column, and then second column
    frame_WCF = Frame([0.088, 0.000, 0.926], [1,0,0], [0, -1,0])
    start_configuration = robot.zero_configuration()

    configuration = robot.inverse_kinematics(frame_WCF, start_configuration)

    print("Found configuration", configuration)
