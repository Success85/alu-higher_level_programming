#!/usr/bin/python3

from sys import argv


def main():
    len_value = len(argv)

    if len_value == 1:
        print("No arguments.")
    elif len_value == 2:
        print("1 argument:")
        print("1:", argv[1])
    else:
        len = len_value - 1
        print(f"{len_value} arguments:")
        i = 1
        while i <= len_value:
            res = argv[i]
            print(f"{i}: {res}")
            i = i + 1


if __name__ == "__main__":
    main()
