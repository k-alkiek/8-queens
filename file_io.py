import numpy as np


def read_config(path):
    with open(path) as f:
        config = [line.strip().split(' ') for line in f.readlines()]

        if np.shape(config) != (8, 8):
            raise Exception("Input configuration is not 8x8")
        return config


def write_config(path, config):
    with open(path, 'w') as f:
        lines = '\n'.join([' '.join(row) for row in config])
        f.write(lines)
