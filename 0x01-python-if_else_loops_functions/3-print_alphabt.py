#!/usr/bin/python
for xup in range(ord('a'), ord('b') + 1):
    if chr(xup) != 'q' and chr(xup) != 'e':
        print("{}".format(chr(xup)), end='')
