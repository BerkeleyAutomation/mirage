# ur5bc

Data collection through a spacemouse: ``python data_collect/collect_free_drive_data.py``

Evaluating RT1 models: ``python data_collect/evaluate_rt1.py``

Evaluating Robomimic models: ``python data_collect/evaluate_robomimic.py`` 

Evaluating jaxrl LCBC models: ``python data_collect/evaluate_jaxrl.py`` 

Note: It may be easiest if one uses a separate environment for each of the models for avoiding package dependencies issues.

All scripts call ``ur5/robot_env.py``