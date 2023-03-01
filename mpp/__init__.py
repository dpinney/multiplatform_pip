import sys
import os
import platform

# global things to know
this_dir = os.path.dirname(__file__)
my_plat = platform.system()

# set up libraries
sys.path.insert(0,this_dir + '/lib/')
if my_plat not in ['Linux', 'Windows', 'Darwin']:
    print(f'Your platform was detected as {my_plat} but we currently only support Linux/Windows/Darwin')
sys.path.insert(0,this_dir + f'/lib/{my_plat}')

# platform-specific imports
import numpy as np

# some simple numpy test code
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[0, 1])