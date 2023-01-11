import sys
import numpy as np
import multiprocessing

n = int(0)
m = int(0)
num_iter = int(0)

start_path = ""
data_path = ""
emit_path = ""
trans_path = ""

if __name__ == '__main__':
    # sys.argv[0] is the name of the program, we can skip it
    n = int(sys.argv[1])  # this takes the 1st terminal argument
    m = int(sys.argv[2])  # this takes the 2nd terminal argument
    num_iter = int(sys.argv[3])
    start_path = sys.argv[4]
    trans_path = sys.argv[5]
    emit_path = sys.argv[6]
    data_path = sys.argv[7]

start = np.loadtxt(start_path, dtype=np.float64)
trans = np.concatenate((np.loadtxt(trans_path, dtype=np.float64), np.zeros(n)[None, :]), axis=0)
emit = np.concatenate((np.loadtxt(emit_path, dtype=np.float64), np.zeros(m)[None, :]), axis=0)

with open(data_path, 'r') as file:
    lines = file.readlines()

data = np.array([])
for line in lines:
    data.append(np.array(line.replace('o', '').split()[:-1], dtype=int))
num_seq = len(data)

