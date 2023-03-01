import os as _os, sys as _sys

this_dir = _os.path.dirname(__file__)
py_bin = _sys.executable

def install():
    # my_plat = 'manylinux2014_x86_64'
    # install_string = f'{py_bin } -m pip install --target="{this_dir}" --platform={my_plat} --only-binary=:all: numpy'
    install_string = f'{py_bin } -m pip install --target="{this_dir}/Linux" --only-binary=:all: numpy'
    _os.system(install_string)

if __name__ == '__main__':
	install()