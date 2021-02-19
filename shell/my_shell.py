'''
Paulie Jo Gonzalez
CS 4375 - os
Lab 1 - part 1
Last modified: 02/14/2021
This code includes a reference to the fork and exec methods provided by Dr. Freudenthal in os-demos.
'''

import os
import sys
import re
import time
from lab_0 import my_read_line

ps1 = '$'  # prompt

while 1:
    os.write(1, ps1.encode())
    # read command
    in_line = my_read_line()

    if in_line.lower() == 'exit' or len(in_line) == 0:
        os.write(2, 'Shell exited\n'.encode())
        sys.exit(1)
    # tokenize command
    tkns = in_line.split(' ')

    # fork a child
    rc = os.fork()

    if rc < 0:
        os.write(2, ('fork failed, exiting shell %d\n' % rc).encode())
        sys.exit(1)
    elif rc == 0:
        # child executes command
        for dir in re.split(':', os.environ['PATH']):   # try each directory
            program = '%s/%s' % (dir, tkns[0])

            try:
                os.execve(program, tkns, os.environ)    # try to exec program
            except FileNotFoundError:
                pass                                    # fail quietly
        os.write(2, ('Child:    failed exec %s\n' % tkns[0]).encode())
        sys.exit(1)  # terminate

    else:
        # parent waits for child to terminate (forked ok)
        os.write(1, ('Parent: My pid=%d. Child pi=%d\n' %
                     (pid, rc)).encode())
        childPidCode = os.wait()
        os.write(1, ('Parent: Child %d terminated with exit code %d\n' %
                     childPidCode).encode())
