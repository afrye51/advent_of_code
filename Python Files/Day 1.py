import numpy as np
import os
import copy


# Given a list of input integers, count how many of the values are larger than the previous value
# Inputs: data_file_name
#       String name of the data file to use as input, assumed to be in ../Data/
def part_1(data_file_name):
    script_dir = os.path.dirname(__file__)
    splt = script_dir.split('/')[:-1]
    splt.append('Data')
    data_dir = "/".join(splt)
    with open(data_dir + '/' + data_file_name) as data_file:
        data = data_file.readlines()
        data = np.array([line.rstrip() for line in data], dtype=int)

    # The strategy: Subtract offset lists, then count the number of values greater than zero
    # List A is the list with the last element duplicated
    list_a = data[1:]
    # List B is the list with the first element duplicated
    list_b = data[:-1]
    # Subtract list B from List A
    diff = list_a - list_b
    # Count the number of values greater than zero
    num_inc = np.sum(diff > 0)
    print(num_inc)


# Given a list of input integers, compute a 3-length moving average and compute how many of the averages are greater
#   than the prior average
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

    data_1 = data[2:]
    data_2 = data[1:-1]
    data_3 = data[:-2]
    data = data_1 + data_2 + data_3

    # The strategy: Subtract offset lists, then count the number of values greater than zero
    # List A is the list with the last element duplicated
    list_a = data[1:]
    # List B is the list with the first element duplicated
    list_b = data[:-1]
    # Subtract list B from List A
    diff = list_a - list_b
    # Count the number of values greater than zero
    num_inc = np.sum(diff > 0)
    print(num_inc)


if __name__ == '__main__':
    part_2("Day 1.csv")
