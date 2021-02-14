'''
Paulie Jo Gonzalez
CS 4375 - os
Lab 1 - part 1
Last modified: 02/14/2021
This code includes a reference to the fork method provided by Dr. Freudenthal in os-demos.
'''

import os
import sys
import re
from lab_0 import my_read_line

ps1 = '$'

while 1:
    os.write(1, ps1.encode())
    in_line = my_read_line()

    if in_line.lower() == 'exit' or len(in_line) == 0:
        os.write(2, 'Shell exited\n'.encode())
        sys.exit(1)

    tkns = in_line.split()

    # fork() code referenced from p1-fork.py from os-demos
    rc = os.fork()

    if rc < 0:
        os.write(2, ('fork failed, exiting %d\n' % rc).encode())
        sys.exit(1)
    elif rc == 0:
        # child executes command
    else:
        # parent waits for child to terminate
        os.wait()
