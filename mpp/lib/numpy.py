import platform

my_plat = platform.system()

if my_plat == 'Linux':
    from numpy_linux import numpy
elif my_plat == 'Windows':
    from numpy_windows import numpy
elif my_play == 'Darwin': #macOS
    from numpy_macos import numpy
else:
    print(f'Your platform was detected as {my_plat} but we currently only support Linux/Windows/Darwin')