from typing import Dict, Any
import tensorflow as tf

def mirage_dataset_transform(trajectory: Dict[str, Any]) -> Dict[str, Any]:
    # NOTE: this is not actually the official OXE copy of bridge, it is our own more up-to-date copy that you
    # can find at https://rail.eecs.berkeley.edu/datasets/bridge_release/data/tfds/
    trajectory["observation"]["proprio"] = tf.concat(
        [
            trajectory["cartesian_position"],
            trajectory["gripper_position"]
        ],
        axis=1,
    )
    print(trajectory["language_instruction"])
    return trajectory