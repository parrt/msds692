"Read numeric table from file argument into numpy array"
import numpy as np
import sys

my_data = np.genfromtxt(sys.argv[1], delimiter=',', skip_header=True)
print type(my_data)
print my_data
