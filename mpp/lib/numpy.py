import platform

my_plat = platform.system()

if my_plat == 'Linux':
    pass
elif my_plat == 'Windows':
    pass
elif my_play == 'Darwin': #macOS
    pass
else:
    print(f'Your platform was detected as {my_plat} but we currently only support Linux/Windows/Darwin')