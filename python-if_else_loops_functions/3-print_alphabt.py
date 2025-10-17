#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    else:
        out = code(i)
        print("{}".format(out), end="")
