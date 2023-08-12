#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # get number of arguments
    arg_count = len(sys.argv) - 1

    arg_total = 0

    for x in range(arg_count):
        arg_total += int(sys.argv[x + 1])
    print("{}".format(arg_total))
