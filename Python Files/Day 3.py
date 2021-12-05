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
    with open(data_dir + '/' + data_file_name) as data_file:
        data = data_file.readlines()
        data = np.array([list(line.rstrip()) for line in data], dtype=int)

    most_common = np.round(np.average(data, axis=0), 0)
    gamma = most_common.dot(2 ** np.arange(most_common.size)[::-1])
    epsilon = np.abs(most_common - 1).dot(2 ** np.arange(most_common.size)[::-1])
    print(gamma)
    print(epsilon)
    print(gamma * epsilon)


# Inputs: data_file_name
#       String name of the data file to use as input, assumed to be in ../Data/
def part_2(data_file_name):
    script_dir = os.path.dirname(__file__)
    splt = script_dir.split('/')[:-1]
    splt.append('Data')
    data_dir = "/".join(splt)
    with open(data_dir + '/' + data_file_name) as data_file:
        data = data_file.readlines()
        data = np.array([line.rstrip() for line in data], dtype=int)

    print('hi')


if __name__ == '__main__':
    data_file_name = "Day 3.csv"
    part_1(data_file_name)
    # part_2(data_file_name)
