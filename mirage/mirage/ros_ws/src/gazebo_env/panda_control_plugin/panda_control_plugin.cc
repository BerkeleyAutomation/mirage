#ifndef _PANDACONTROL_PLUGIN_HH_
#define _PANDACONTROL_PLUGIN_HH_

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo_ros/node.hpp>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/float64_multi_array.hpp>
#include <sensor_msgs/msg/joint_state.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h> 
#include <cv_bridge/cv_bridge.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
namespace gazebo
{
  /// \brief A plugin to control a NoPhysics sensor.
  class PandaControlPlugin : public ModelPlugin
  {
    /// \brief Constructor
    public: PandaControlPlugin() {}

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
      std::cerr << "KUSHTIMUS PRIME PANDA" << "\n";
      this->robot_subscriber_ = this->node_->create_subscription<std_msgs::msg::Float64MultiArray>(
                "joint_commands",
                qos.get_subscription_qos("joint_commands", rclcpp::QoS(1)),
                std::bind(&PandaControlPlugin::jointCommandMsg, this, std::placeholders::_1));
      this->gazebo_joint_state_publisher_ = this->node_->create_publisher<sensor_msgs::msg::JointState>("/gazebo_joint_states",1);

      // ROS2 Message Filter Tutorial: https://answers.ros.org/question/366440/ros-2-message_filters-timesynchronizer-minimal-example-does-not-reach-callback-function/
      rclcpp::QoS qos_(1);
      auto rmw_qos_profile = qos_.get_rmw_qos_profile();
      this->rgb_subscriber_.subscribe(this->node_, "/panda_camera/image_raw", rmw_qos_profile);
      this->depth_subscriber_.subscribe(this->node_, "/panda_camera/depth/image_raw", rmw_qos_profile);
      this->time_synchronizer_ = std::make_shared<message_filters::TimeSynchronizer<sensor_msgs::msg::Image, sensor_msgs::msg::Image>>(rgb_subscriber_, depth_subscriber_,1);
      this->time_synchronizer_->registerCallback(std::bind(&PandaControlPlugin::imageCallback, this, std::placeholders::_1, std::placeholders::_2));

    }

    //Needs to be const ConstSharedPtr: https://robotics.stackexchange.com/questions/102503/ros2-message-filters-synchronizer-compilation-error
    void imageCallback(const sensor_msgs::msg::Image::ConstSharedPtr rgb_msg,const sensor_msgs::msg::Image::ConstSharedPtr depth_msg) {
      this->rgb_msg_ = rgb_msg;
      this->depth_msg_ = depth_msg;
    }
    void jointCommandMsg(const std_msgs::msg::Float64MultiArray::SharedPtr msg) {
        std::cout << "Start publish" << std::endl;
        physics::WorldPtr world = physics::get_world("default");
        auto model_ptr = world->ModelByName(model_name_);
        auto panda_joint1 = model_ptr->GetJoint("panda_joint1");
        auto panda_joint2 = model_ptr->GetJoint("panda_joint2");
        auto panda_joint3 = model_ptr->GetJoint("panda_joint3");
        auto panda_joint4 = model_ptr->GetJoint("panda_joint4");
        auto panda_joint5 = model_ptr->GetJoint("panda_joint5");
        auto panda_joint6 = model_ptr->GetJoint("panda_joint6");
        auto panda_joint7 = model_ptr->GetJoint("panda_joint7");
        auto panda_finger_joint1 = model_ptr->GetJoint("panda_finger_joint1");
        auto panda_finger_joint2 = model_ptr->GetJoint("panda_finger_joint2");
        // Needs to coordinate with custon_joint_state_publisher_node.py
        panda_joint1->SetPosition(0,msg->data[0]);
        panda_joint2->SetPosition(0,msg->data[1]);
        panda_joint3->SetPosition(0,msg->data[2]);
        panda_joint4->SetPosition(0,msg->data[3]);
        panda_joint5->SetPosition(0,msg->data[4]);
        panda_joint6->SetPosition(0,msg->data[5]);
        panda_joint7->SetPosition(0,msg->data[6]);
        panda_finger_joint1->SetPosition(0,msg->data[7]);
        panda_finger_joint2->SetPosition(0,msg->data[7]);
        auto message = sensor_msgs::msg::JointState();
        message.header.stamp = this->node_->get_clock() ->now();
        message.name = {"panda_joint1","panda_joint2","panda_joint3","panda_joint4","panda_joint5","panda_joint6","panda_joint7","panda_finger_joint1","panda_finger_joint2"};
        message.position = {msg->data[0],msg->data[1],msg->data[2],msg->data[3],msg->data[4],msg->data[5],msg->data[6],msg->data[7]};
        //Delay for image to catch up to joint position update
        //usleep(100000);
        this->gazebo_joint_state_publisher_->publish(message);
        std::cout << "Finished publish" << std::endl;
    }


    private:
      gazebo_ros::Node::SharedPtr node_;
      std::string model_name_;
      rclcpp::Subscription<std_msgs::msg::Float64MultiArray>::SharedPtr robot_subscriber_;
      rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr gazebo_joint_state_publisher_;
      message_filters::Subscriber<sensor_msgs::msg::Image> rgb_subscriber_;
      message_filters::Subscriber<sensor_msgs::msg::Image> depth_subscriber_;
      std::shared_ptr<message_filters::TimeSynchronizer<sensor_msgs::msg::Image, sensor_msgs::msg::Image>> time_synchronizer_;
      sensor_msgs::msg::Image::ConstSharedPtr rgb_msg_;
      sensor_msgs::msg::Image::ConstSharedPtr depth_msg_;
      
  };

  // Tell Gazebo about this plugin, so that Gazebo can call Load on this plugin.
  GZ_REGISTER_MODEL_PLUGIN(PandaControlPlugin)
}
#endif
