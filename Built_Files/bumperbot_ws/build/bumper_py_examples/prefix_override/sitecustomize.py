import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/madison/Documents/Firmware/bumperbot_ws/install/bumper_py_examples'
