#!/usr/bin/python3
def print_last_digit(number):
    output = abs(number)
    lastnum = output % 10
    print("{}".format(lastnum), end="")
    return(lastnum)
