#!/usr/bin/env python3

import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def unix_time(function):
    '''Return `real`, `sys`, and `user` elapsed time, like UNIX's command `time`.
    You can calculate the amount of CPU time used by summing `user` and `sys`.
    `real` is similar to the wall clock.
    Note: Resolutions of `user` and `sys` are limited by the OS's software clock.
    '''
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    return "\nreal: {}\nuser: {}\nsys: {}".format(
        end_time - start_time,
        end_resources.ru_utime - start_resources.ru_utime,
        end_resources.ru_stime - start_resources.ru_stime)

def print_factors():
    fun = ctypes.CDLL("./lib_factors.so")
    fun.trial_division.argtypes = [ctypes.c_long]
    
    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line.strip())
            fun.trial_division(n)
            line = prime.readline()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factors.py <file>")
        sys.exit(1)

    print(unix_time(print_factors))
