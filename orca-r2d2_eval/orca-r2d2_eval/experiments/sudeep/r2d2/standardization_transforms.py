"""Episode transforms for custom (non-OXE) RLDS datasets to canonical dataset definition."""
from typing import Any, Dict

import tensorflow as tf
import numpy as np
import tensorflow_graphics.geometry.transformation as tfg


def rmat_to_euler(rot_mat):
    return tfg.euler.from_rotation_matrix(rot_mat)


def euler_to_rmat(euler):
    return tfg.rotation_matrix_3d.from_euler(euler)


def invert_rmat(rot_mat):
    return tfg.rotation_matrix_3d.inverse(rot_mat)


def mat_to_rot6d(mat):
    r6 = mat[..., :2, :]
    r6_0, r6_1 = r6[..., 0, :], r6[..., 1, :]
    r6_flat = tf.concat([r6_0, r6_1], axis=-1)
    return r6_flat


def change_velocity_frame(velocity, frame):
    R_frame = euler_to_rmat(frame[:, 3:6])
    R_frame_inv = invert_rmat(R_frame)

    # world to wrist: dT_pi = R^-1 dT_rbt
    vel_t = (R_frame_inv @ velocity[:, :3][..., None])[..., 0]

    # world to wrist: dR_pi = R^-1 dR_rbt R
    dR = euler_to_rmat(velocity[:,3:6])
    dR = R_frame_inv @ (dR @ R_frame)
    dR_r6 = mat_to_rot6d(dR)
    return tf.concat([vel_t, dR_r6], axis=-1)


def r2_d2_dataset_transform(trajectory: Dict[str, Any]) -> Dict[str, Any]:
    # every input feature is batched, ie has leading batch dimension
    trajectory["action"] = tf.concat(
        (
            trajectory["action_dict"]["cartesian_velocity"],
            trajectory["action_dict"]["gripper_position"],
        ),
        axis=-1,
    )
    return trajectory


def r2_d2_dataset_wristact_transform(trajectory: Dict[str, Any]) -> Dict[str, Any]:
    # every input feature is batched, ie has leading batch dimension
    wrist_act = change_velocity_frame(
        trajectory["action_dict"]["cartesian_velocity"],
        trajectory["observation"]["cartesian_position"]
    )
    trajectory["action"] = tf.concat(
        (
            wrist_act,
            trajectory["action_dict"]["gripper_position"],
        ),
        axis=-1,
    )
    return trajectory
