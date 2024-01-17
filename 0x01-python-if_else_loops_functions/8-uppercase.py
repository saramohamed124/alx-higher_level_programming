#!/usr/bin/python3
def islower(c):
    if ord >= ord('a') and ord(c) <= ord('z'):
        return False
    else:
        return True

def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) if not islower(c) else ord(c) - 32, end="")
        print("")
