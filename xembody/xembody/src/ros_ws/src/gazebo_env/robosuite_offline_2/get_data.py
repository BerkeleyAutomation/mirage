import numpy as np

# Load the data
data = np.load("one_trajectory_source_target.npy", allow_pickle=True)
dict_str = str(data[0])

# Write the dictionary string to a text file
with open('first_part.txt', 'w') as file:
    file.write(dict_str)