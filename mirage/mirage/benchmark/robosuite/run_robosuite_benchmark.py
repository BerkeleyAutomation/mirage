from mirage.benchmark.robosuite.robosuite_experiment_config import ExperimentRobotsuiteConfig
from mirage.benchmark.robosuite.robosuite_experiment import RobosuiteExperiment

import argparse

def main():
    parser = argparse.ArgumentParser(description="Mirage Robosuite Benchmark")
    parser.add_argument("--config_file", type=str)
    args = parser.parse_args()

    print("Loading config from: ", args.config_file)
    config = ExperimentRobotsuiteConfig.from_yaml(args.config_file)
    print(config)
    should_launch = input("Launch the experiment? [Y/n] ")
    if should_launch.lower() != "y":
        print("Exiting...")
        return

    new_experiment = RobosuiteExperiment(config)
    
    try:
        new_experiment.launch()
    except ValueError as e:
        should_override = input("Results folder already exists. Override? [Y/n] ")
        if should_override.lower() != "y":
            print("Exiting...")
            return
        new_experiment.launch(override=True)

    source_results, target_results = new_experiment.get_results(blocking=True)
    print("Source Results:")
    print(source_results)
    print("Target Results:")
    print(target_results)

if __name__ == "__main__":
    main()