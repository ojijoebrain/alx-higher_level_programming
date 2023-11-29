#!/usr/bin/python3
for value in range(122, 96, -1):
    a = value
    if (value % 2) == 1:
        a -= 32
    print('{:s}'.format(chr(a)), end='')
