import os as _os, sys as _sys, platform as _platform
this_dir = _os.path.dirname(__file__)
py_bin = _sys.executable

try:
    from mpp.lib import numpy as np
except:
    print('mpp: requirements missing. performing first time setup.')
    install_string = f'{py_bin } -m pip install --target="{this_dir}/lib/" numpy'
    _os.system(install_string)

# old approach please ignore.
# this_dir = os.path.dirname(__file__)
# my_plat = platform.system()
# sys.path.insert(0,this_dir + '/lib/')
# if my_plat not in ['Linux', 'Windows', 'Darwin']:
#     print(f'Your platform was detected as {my_plat} but we currently only support Linux/Windows/Darwin')
# print(f'Platform detected: {my_plat}')
# sys.path.insert(0,this_dir + f'/lib/{my_plat}')
# print(f'New path: {sys.path}')

# TODO: think about pure python approach.
# how about a pure python lib?
# import flask

# some simple numpy test code
print('numpy test:')
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[0, 1])