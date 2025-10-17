#!/usr/bin/python3
from sys import argv


def main():
    num = 0
    for i in argv[1:]:
        i = int(i)
        num = num + i

    print(num)


if __name__ == "__main__":
    main()
