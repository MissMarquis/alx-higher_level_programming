#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError, NameError):
        return (False)
    else:
        return (True)
