# Mirage
<p align="center">
  <picture>
    <img src="https://github.com/BerkeleyAutomation/mirage/assets/52500655/3d724f08-48da-4d7d-9693-09f76dd4eefd">
  </picture>
</p>

This repository contains the official implementation of Mirage, a novel zero-shot cross-embodiment policy transfer method that uses cross-painting to bridge the visual gap and forward dynamics to bridge the control gap. There is also benchmarking code for across a variety of cross-embodiment scenariors with different robots, tasks, and simulators. Please know that the repo is under active development, please see progress [here](https://github.com/BerkeleyAutomation/mirage/issues/6). 

## Supported Robots, Tasks, and Simulators
<p align="center">
  <picture>
    <img src="https://github.com/BerkeleyAutomation/mirage/assets/52500655/0c566742-b398-4c84-b6ec-98ee68245c68">
  </picture>
</p>

## Getting Started
The in-depth documentation for Mirage is found [here](https://berkeleyautomation.github.io/mirage/).

Clone the repo:
```
git clone --recurse-submodules git@github.com:BerkeleyAutomation/mirage.git
```

Install ROS 2 and setup the Gazebo Environment for Inpainting by following the instructions in `mirage/mirage/ros_ws/src/README.md` 

Create a conda environment and install the mirage Python package.
```
conda create -n mirage --python=3.10
cd mirage
pip install -e .
```

Follow the installation instructions for the downloaded robomimic, robosuite, and mimicgen_environments submodules by going into them and looking at the README.

Build the ROS workspace by running (from the root of this repo)
```
cd mirage/mirage/ros_ws
colcon build
source install/setup.bash
```

## Usage
### Robosuite Benchmark
If inpainting is enabled, only 1 benchmarking process can be run at a given time.
Depending on the robosuite environment, the ros launch file will be different due to different camera extrinsics.
Firstly, in one terminal, run the gazebo writer node
```
source mirage/mirage/ros_ws/install/setup.bash
ros2 run gazebo_env write_data_node_robosuite_better.py
```

Then, launch the gazebo process for the corresponding environment by first running (in a new terminal):
```
source mirage/mirage/ros_ws/install/setup.bash
```
Run either one of these depending on the environment (three piece assembly is really two piece assembly).
```
ros2 launch gazebo_env panda_gazebo_classic_robosuite_can.launch.py
ros2 launch gazebo_env panda_gazebo_classic_robosuite_lift_square_stack_three_threading.launch.py
ros2 launch gazebo_env panda_gazebo_classic_robosuite_three_piece_assembly.launch.py
```

For robosuite, to run an experiment (from the root of this repo), 
```
# Run this command below if inpainting, otherwise skip
source mirage/mirage/ros_ws/install/setup.bash

cd mirage/mirage/benchmark/robosuite
python3 run_robosuite_benchmark.py --config config/example_config.yaml
```
Please take a look at the example_config and the different parameters that can be set to run different tasks, agents, and robots. For the above code to work, you must change the agents to the path for the model checkpoints in robosuite.

## Citation
If you utilized the benchmark, please consider citing the paper:
```
@misc{chen2024mirage,
      title={Mirage: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting}, 
      author={Lawrence Yunliang Chen and Kush Hari and Karthik Dharmarajan and Chenfeng Xu and Quan Vuong and Ken Goldberg},
      year={2024},
      eprint={2402.19249},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```

## Contributing
Feel free to raise any concerns and bugs through the [issue](https://github.com/BerkeleyAutomation/mirage/issues) portal, and submit PR with your own edits. Please reach out if some abstractions of features do not meet your needs, we are very eager to help with implementation.