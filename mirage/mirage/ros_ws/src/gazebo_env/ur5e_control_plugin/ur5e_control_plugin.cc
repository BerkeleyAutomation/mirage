#ifndef _UR5ECONTROL_PLUGIN_HH_
#define _UR5ECONTROL_PLUGIN_HH_

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo_ros/node.hpp>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/float64_multi_array.hpp>

namespace gazebo
{
  /// \brief A plugin to control a NoPhysics sensor.
  class UR5eControlPlugin : public ModelPlugin
  {
    /// \brief Constructor
    public: UR5eControlPlugin() {}

    /// \brief The load function is called by Gazebo when the plugin is
    /// inserted into simulation
    /// \param[in] _model A pointer to the model that this plugin is
    /// attached to.
    /// \param[in] _sdf A pointer to the plugin's SDF element.
    public: virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      // Initialize ROS node
      this->node_ = gazebo_ros::Node::Get(_sdf);
      this->model_name_ = _model->GetName();
      const gazebo_ros::QoS &qos = this->node_->get_qos();
      // Just output a message for now
      std::cerr << "KUSHTIMUS PRIME UR5" << "\n";
      this->robot_subscriber_ = this->node_->create_subscription<std_msgs::msg::Float64MultiArray>(
                "joint_commands",
                qos.get_subscription_qos("joint_commands", rclcpp::QoS(1)),
                std::bind(&UR5eControlPlugin::jointCommandMsg, this, std::placeholders::_1));
    }

    void jointCommandMsg(const std_msgs::msg::Float64MultiArray::SharedPtr msg) {
        physics::WorldPtr world = physics::get_world("default");
        auto model_ptr = world->ModelByName(model_name_);
        auto shoulder_pan_joint = model_ptr->GetJoint("shoulder_pan_joint");
        auto shoulder_lift_joint = model_ptr->GetJoint("shoulder_lift_joint");
        auto elbow_joint = model_ptr->GetJoint("elbow_joint");
        auto wrist_1_joint = model_ptr->GetJoint("wrist_1_joint");
        auto wrist_2_joint = model_ptr->GetJoint("wrist_2_joint");
        auto wrist_3_joint = model_ptr->GetJoint("wrist_3_joint");
        auto left_knuckle = model_ptr->GetJoint("robotiq_85_left_knuckle_joint");
        auto right_knuckle = model_ptr->GetJoint("robotiq_85_right_knuckle_joint");
        auto left_inner_knuckle = model_ptr->GetJoint("robotiq_85_left_inner_knuckle_joint");
        auto right_inner_knuckle = model_ptr->GetJoint("robotiq_85_right_inner_knuckle_joint");
        auto left_finger = model_ptr->GetJoint("robotiq_85_left_finger_tip_joint");
        auto right_finger = model_ptr->GetJoint("robotiq_85_right_finger_tip_joint");
        // Needs to coordinate with custon_joint_state_publisher_node.py
        shoulder_pan_joint->SetPosition(0,msg->data[0]);
        shoulder_lift_joint->SetPosition(0,msg->data[1]);
        elbow_joint->SetPosition(0,msg->data[2]);
        wrist_1_joint->SetPosition(0,msg->data[3]);
        wrist_2_joint->SetPosition(0,msg->data[4]);
        wrist_3_joint->SetPosition(0,msg->data[5]);
        left_knuckle->SetPosition(0,msg->data[6]);
        right_knuckle->SetPosition(0,msg->data[6]);
        left_inner_knuckle->SetPosition(0,msg->data[6]);
        right_inner_knuckle->SetPosition(0,msg->data[6]);
        left_finger->SetPosition(0,-msg->data[6]);
        right_finger->SetPosition(0,-msg->data[6]);
    }


    private:
      gazebo_ros::Node::SharedPtr node_;
      std::string model_name_;
      rclcpp::Subscription<std_msgs::msg::Float64MultiArray>::SharedPtr robot_subscriber_;
      
  };

  // Tell Gazebo about this plugin, so that Gazebo can call Load on this plugin.
  GZ_REGISTER_MODEL_PLUGIN(UR5eControlPlugin)
}
#endif
