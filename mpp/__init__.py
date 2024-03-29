import os as _os, sys as _sys, platform as _platform

# setup environment
this_dir = _os.path.dirname(__file__)
py_bin = _sys.executable
_sys.path.insert(0, this_dir + '/lib/')

# platform-specific imports
try:
    import numpy as np
except Exception:
    print('mpp: requirements missing. performing first time setup.')
    install_string = f'{py_bin} -m pip install --target="{this_dir}/lib/" numpy'
    _os.system(install_string)
    import numpy as np

# TODO: think about approach for pure python... just bundle directly?
# import flask

_os.system('ls -alh')

# some simple numpy test code
print('numpy test:')
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[0, 1])
