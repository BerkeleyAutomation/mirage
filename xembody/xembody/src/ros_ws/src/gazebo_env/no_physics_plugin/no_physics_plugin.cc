#ifndef _NOPHYSICS_PLUGIN_HH_
#define _NOPHYSICS_PLUGIN_HH_

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo_ros/node.hpp>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/float64_multi_array.hpp>

namespace gazebo
{
  /// \brief A plugin to control a NoPhysics sensor.
  class NoPhysicsPlugin : public ModelPlugin
  {
    /// \brief Constructor
    public: NoPhysicsPlugin() {}

    /// \brief The load function is called by Gazebo when the plugin is
    /// inserted into simulation
    /// \param[in] _model A pointer to the model that this plugin is
    /// attached to.
    /// \param[in] _sdf A pointer to the plugin's SDF element.
    public: virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      // Initialize ROS node
      this->node_ = gazebo_ros::Node::Get(_sdf);
      const gazebo_ros::QoS &qos = this->node_->get_qos();
      // Just output a message for now
      std::cerr << "NO PHYSICS" << "\n";
      _model->GetWorld()->SetPhysicsEnabled(false);
      //light_ptr -> Fini();
    }


    private:
      bool green_box_ = false;
      std::string red_box_name_ = "my_model1";
      std::string green_box_name_ = "";
      int name_length_ = 9;
      int i_ = -1;
      int length_ = 3;
      float x_[3] = {0.4,-0.5,0.817};
      float y_[3] = {0.4,0.6,0.233};
      float z_[3] = {0.4,0.3,0.063};
      gazebo_ros::Node::SharedPtr node_;
      rclcpp::Subscription<std_msgs::msg::String>::SharedPtr ee_pose_subscriber_;
      rclcpp::Subscription<std_msgs::msg::Float64MultiArray>::SharedPtr command_subscriber_;
      rclcpp::Publisher<std_msgs::msg::String>::SharedPtr ee_pose_publisher_;
      bool set_position_ = false;
      std::string original_box_str_ = "<?xml version='1.0'?>\n"
"<sdf version=\"1.4\">\n"
"  <model name=\"my_model1\">\n"
"    <pose>0 0 0 0 0 0</pose>\n"
"    <static>true</static>\n"
"    <link name=\"link\">\n"
"      <inertial>\n"
"        <mass>1.0</mass>\n"
"        <inertia> <!-- inertias are tricky to compute -->\n"
"          <!-- http://gazebosim.org/tutorials?tut=inertia&cat=build_robot -->\n"
"          <ixx>0.083</ixx>       <!-- for a box: ixx = 0.083 * mass * (y*y + z*z) -->\n"
"          <ixy>0.0</ixy>         <!-- for a box: ixy = 0 -->\n"
"          <ixz>0.0</ixz>         <!-- for a box: ixz = 0 -->\n"
"          <iyy>0.083</iyy>       <!-- for a box: iyy = 0.083 * mass * (x*x + z*z) -->\n"
"          <iyz>0.0</iyz>         <!-- for a box: iyz = 0 -->\n"
"          <izz>0.083</izz>       <!-- for a box: izz = 0.083 * mass * (x*x + y*y) -->\n"
"        </inertia>\n"
"      </inertial>\n"
"      <collision name=\"collision\">\n"
"        <geometry>\n"
"          <box>\n"
"            <size>0.05 0.05 0.05</size>\n"
"          </box>\n"
"        </geometry>\n"
"      </collision>\n"
"      <visual name=\"visual\">\n"
"        <geometry>\n"
"          <box>\n"
"            <size>0.05 0.05 0.05</size>\n"
"          </box>\n"
"        </geometry>\n"
"        <material>\n"
"          <script>\n"
"            <uri>file:///usr/share/gazebo-11/media/materials/scripts/gazebo.material</uri>\n"
"            <name>Gazebo/Red</name>\n"
"          </script>\n"
"        </material>\n"
"      </visual>\n"
"    </link>\n"
"  </model>\n"
"</sdf>";
      std::string current_box_str = original_box_str_; 
      
  };

  // Tell Gazebo about this plugin, so that Gazebo can call Load on this plugin.
  GZ_REGISTER_MODEL_PLUGIN(NoPhysicsPlugin)
}
#endif
