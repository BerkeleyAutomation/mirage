import subprocess
import xml.etree.ElementTree as ET
xacro_command = "ros2 run xacro xacro /home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/ur5e_gazebo.urdf.xacro"
xacro_subprocess = subprocess.Popen(
    xacro_command,
    shell=True,
    stdout=subprocess.PIPE,
)
urdf_string = ""
while True:
    line = xacro_subprocess.stdout.readline()
    if line:
        line_byte = line.strip()
        line = line_byte.decode("utf-8")
        urdf_string += line
    else:
        break
root = ET.fromstring(urdf_string)
for link in root.iter('link'):
    element_name1 = "visual"
    found_element1 = link.find(".//" + element_name1)
    element_name2 = "geometry"
    found_element2 = link.find(".//" + element_name2)
    element_name3 = "mesh"
    found_element3 = link.find(".//" + element_name3)
    if (found_element1 is not None) and (found_element2 is not None) and (found_element3 is not None):
        link_name = link.attrib.get('name')
        for visual in link.iter("visual"):
            origin_element = visual.find(".//origin")
            print(origin_element.attrib)
            for geometry in visual.iter("geometry"):
                for mesh in geometry.iter("mesh"):
                    filename = mesh.attrib.get('filename')[7:]
                    print(link_name)
