'''
Paulie Jo Gonzalez
CS 4375 - os
Lab 0
Last modified: 02/14/2021
This code includes a reference to C code for my_getChar method provided by Dr. Freudenthal.
'''

from os import read

next_c = 0
limit = 0


def get_char():
    global next_c, limit

    if next_c == limit:
        next_c = 0
        limit = read(0, 100)        # allocate bytes

        if limit == 0:
            return ''

    if next_c >= len(limit) - 1:    # check upperbound
        return ''
    ch = chr(limit[next_c])         # convert to char (from ASCII)
    next_c += 1

    return ch


def my_read_line():
    global next_c, limit

    line = ''
    ch = get_char()

    # get each char of line
    while (ch != '\n'):              # while char is not new line
        line += ch                   # build line
        ch = get_char()
        if ch == '':
            return line             # EOF

    next_c = 0                      # reset next_c and limit after line is read
    limit = 0
    line += '\n'

    return line


# def my_read_lines():
#     num_lines = 0
#     in_line = my_read_line()       # read line

#     while len(in_line):
#         num_lines += 1
#         print(f'###line {num_lines}: <{str(in_line)}> ###\n')

#         in_line = my_read_lines()
#         print(f'eof after {num_lines}\n')
