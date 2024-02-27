from xembody_robosuite.benchmark.robosuite_experiment_config import ExperimentRobotsuiteConfig
from xembody_robosuite.benchmark.robosuite_experiment import RobosuiteExperiment

import argparse

def main():
    parser = argparse.ArgumentParser(description="Mirage Robosuite Benchmark")
    parser.add_argument("--config_file", type=str)
    args = parser.parse_args()

    config = ExperimentRobotsuiteConfig.from_yaml(args.config_file)
    print("Config: ", config)
    should_launch = input("Launch the experiment? [Y/n]")
    if should_launch.lower() != "y":
        print("Exiting...")
        return

    new_experiment = RobosuiteExperiment(config)
    new_experiment.launch()

    source_results, target_results = new_experiment.get_results(blocking=True)
    print("Source Results:")
    print(source_results)
    print("Target Results:")
    print(target_results)