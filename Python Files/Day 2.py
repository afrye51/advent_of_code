import numpy as np
import os
import copy


# Inputs: data_file_name
#       String name of the data file to use as input, assumed to be in ../Data/
def part_1(data_file_name):
    script_dir = os.path.dirname(__file__)
    splt = script_dir.split('/')[:-1]
    splt.append('Data')
    data_dir = "/".join(splt)
    dir_dict = {'forward': np.array([1, 0]), 'down': np.array([0, 1]), 'up': np.array([0, -1])}

    with open(data_dir + '/' + data_file_name) as data_file:
        data = data_file.readlines()
        data = np.array([(dir_dict[line.split()[0]] * int(line.split()[1])) for line in data], dtype=int)

    totals = np.sum(data, axis=0)
    print(totals)
    print(totals[0] * totals[1])


# Inputs: data_file_name
#       String name of the data file to use as input, assumed to be in ../Data/
def part_2(data_file_name):
    script_dir = os.path.dirname(__file__)
    splt = script_dir.split('/')[:-1]
    splt.append('Data')
    data_dir = "/".join(splt)
    dir_dict = {'forward': np.array([1, 0]), 'down': np.array([0, 1]), 'up': np.array([0, -1])}

    with open(data_dir + '/' + data_file_name) as data_file:
        data = data_file.readlines()
        data = np.array([(dir_dict[line.split()[0]] * int(line.split()[1])) for line in data], dtype=int)

    sums = np.array([np.cumsum(data[:, 1])]).T
    data = np.hstack((data, np.array([np.cumsum(data[:, 1])]).T))

    forward = np.sum(data[:, 0], axis=0)
    depth = np.sum(np.prod(data[:, [0, 2]], axis=1))
    totals = [forward, depth]
    print(totals)
    print(totals[0] * totals[1])


if __name__ == '__main__':
    data_file_name = "Day 2.csv"
    part_1(data_file_name)
    part_2(data_file_name)
