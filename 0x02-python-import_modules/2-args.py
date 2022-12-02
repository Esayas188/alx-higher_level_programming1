#!/usr/bin/python3
if __name == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_count = len(argv)
    index = 1
    if arg_count is 0:
        print("{:d} arguments.".format(argv_count))
    elif arg_count is 1:
        print("{:d} argument.".format(argv_count))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments.".format(argv_count))
        while i < argv_count:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
