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
from my_redirect import redirect
from my_pipe import pipe

ps1 = '$ '  # prompt
pid = os.getpid()               # get and remember pid

while 1:
    os.write(1, ps1.encode())
    # read command
    in_line = my_read_line()

    # tokenize input
    args = in_line.split(' ')

    if args[0] == 'exit':
        os.write(2, 'shell exited\n'.encode())
        # successful termination (0 -> clean exit, 1 -> exited with error)
        sys.exit(0)

    elif args[0] == 'cd':
        try:
            if(len(args) == 1):
                continue
            else:
                # chdir -> change current working directory to specified path
                os.chdir(args[1])
        except:
            os.write(1('cd: no such file or directory: %s\n' % args[1]))

    else:
        # fork a child: create a new process
        rc = os.fork()

        if rc < 0:      # fork failed
            os.write(2, ('fork failed, exiting shell %d\n' % rc).encode())
            sys.exit(1)  # exited with error, unsuccessful termination
        elif rc == 0:   # fork successful
            if '<' in args or '>' in args:
                redirect(args)  # redirect to indicator
            elif '|' in args:
                pipe_input(args)  # pipe

            else:
                for dir in re.split(':', os.environ['PATH']):
                    program = '%s/%s' % (dir, args[0])

                    try:
                        # try to exec program
                        os.execve(program, args, os.environ)
                    except FileNotFoundError:
                        pass                                    # fail quietly
                os.write(2, ('%s: could not execute\n' % args[0])).endcode())
                sys.exit(1)

        else:
            # parent waits for child to terminate (forked ok)
            os.write(1, ('Parent: My pid=%d. Child pi=%d\n' %
                         (pid, rc)).encode())
            childPidCode=os.wait()
            os.write(1, ('Parent: Child %d terminated with exit code %d\n' %
                         childPidCode).encode())
