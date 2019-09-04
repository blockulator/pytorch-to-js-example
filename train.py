import random
import math
import numpy as np

# random value 0 < x < 2Pi
def tau_rand(x):
    return random.uniform(0, 2 * math.pi)

# map function and convert to list
def lmap(func, data):
    return list(map(func, data))

# No. of data items for training and for testing
train_data_size = 100000
test_data_size = 8000

# create arrays of random values 0 < x < 2Pi
in_data_x_train = lmap(tau_rand, [0] * train_data_size)
in_data_x_test = lmap(tau_rand, [0] * test_data_size)

# sin and cos values to lean from training data
out_data_u_train = lmap(math.sin, in_data_x_train)
out_data_v_train = lmap(math.cos, in_data_x_train)

# sin and cos values to test learned model against
out_data_u_test = lmap(math.sin, in_data_x_test)
out_data_v_test = lmap(math.cos, in_data_x_test)

# convert data to numpy tables
in_data_train = np.row_stack(in_data_x_train)
in_data_test = np.row_stack(in_data_x_test)

out_data_train = np.column_stack((out_data_u_train, out_data_v_train))
out_data_test = np.column_stack((out_data_u_test, out_data_v_test))
