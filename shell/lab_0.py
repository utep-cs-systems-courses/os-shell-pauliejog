'''
Paulie Jo Gonzalez
CS 4375 - os
Lab 0
Last modified: 02/13/2021
This code includes a reference to C code for my_getChar method provided by Dr. Freudenthal.
'''

from os import read

next_c = 0
limit = 0


def get_char():
    global next_c, limit

    if next_c == limit:
        next_c = 0
        limit = read(0, 100)

        if limit == 0:
            return 'EOF'

    # next_c oob
    if next_c > len(limit) - 1:
        return 'EOF'

    ch = chr(limit[next_c])
    next_c += 1
    return ch


def my_read_line():
    global next_c, limit

    line = ''
    ch = get_char()

    while(ch != '' and ch != 'EOF'):
        line += ch
        ch = get_char

    next_c = 0
    limit = 0

    return line
