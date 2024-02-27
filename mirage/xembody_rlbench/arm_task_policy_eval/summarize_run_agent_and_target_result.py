import numpy as np
tasks = ["take_lid_off_saucepan", "open_door", "lamp_on", "take_umbrella_out_of_umbrella_stand", "toilet_seat_up", "pick_up_cup"]
robots = ["ur5", "sawyer"]

for task in tasks:
    for robot in robots:
        result = np.loadtxt(f"eval_data/systematic/C2FARM_{task}_panda_{robot}_50_trajs.txt", delimiter=",")
        print(task, robot)
        print(result.mean(axis=0))
        
        
"""
take_lid_off_saucepan 
ur5: [24.5   1.    0.24  1.  ]
sawyer: [27.2   1.    0.86  0.92]

open_door 
ur5: [178.14   0.92   0.82   0.54]
sawyer: [825.64 0.86 0.84 0.46]

lamp_on 
ur5: [27.78  0.88  0.52  0.68]
sawyer: [28.68  0.92  0.78  0.7 ]

take_umbrella_out_of_umbrella_stand 
ur5: [50.02  0.94  0.8   0.52]
sawyer: [36.8   0.96  0.76  0.46]

toilet_seat_up 
ur5: [197.62   0.76   0.4    0.2 ]
sawyer: [121.38   0.78   0.86   0.8 ]

pick_up_cup 
ur5: [41.4   0.94  0.22  0.18]
sawyer: [38.62  0.82  0.18  0.06]
"""