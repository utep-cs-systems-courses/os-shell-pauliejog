import os
import sys


def redirect(arg):
    if '<' in args:  # input redirection (stdin)
        os.close(0)  # close file descriptor 0, remomve from keyboard
        os.open(arg[args.index('<')+1], os.O_RDONLY)    # write only
        os.set_inheritable(0, True)

        args.remove(args[args.index('<')+1])    # already used
        args.remove('<')                        # already used

    elif '>' in args:   # output redirection (stdout)
        os.close(1)
        # out file, create or write to existing
        os.open(args[args.index('>')+1], os.O_WRONLY | os.O_CREAT)
        os.set_inheritable(1, True)

        args.remove(args[args.index('>')+1])    # already used
        args.remove('>')                        # already used

    # try each directory in path
    for dir in re.split(':', os.environ['PATH']):
        program = '%s/%s' % (dir, args[0])

        try:
            # try to exec program
            os.execve(program, args, os.environ)
        except FileNotFoundError:
            pass                                    # fail quietly
