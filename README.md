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

Create a conda environment or virtualenv:
```
conda create --name mirage python=3.8
```

Install the mirage Python package.
```
cd mirage
pip install -e .
```

Follow the installation instructions for the given simulator by going into the forked repositories.

## Usage
For robosuite, to run an experiment, 
```
cd mirage/benchmark/robosuite
python3 run_robosuite_benchmark.py --config_file config/example_config.yaml
```
Please take a look at the example_config and the different parameters that can be set to run different tasks, agents, and robots. For the above code to work, you must change the agents to the path for the model checkpoints in robosuite.

## Citation
If you utilized the benchmark, please consider citing the paper:
```
TODO: Add link to ArXiv / publication
```

## Contributing
Feel free to raise any concerns and bugs through the [issue](https://github.com/BerkeleyAutomation/mirage/issues) portal, and submit PR with your own edits. Please reach out if some abstractions of features do not meet your needs, we are very eager to help with implementation.