#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------


# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import csv


import sys

def process_line(line):
    fields = line.strip().split(",")
    start_station_name = fields[4]
    stop_station_name = fields[8]
    return (start_station_name, 1), (stop_station_name, 1)

def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters=None):
    results = {}
    for line in my_input_stream:
        (start_station, start_count), (stop_station, stop_count) = process_line(line)
        if start_station not in results:
            results[start_station] = (0, 0)
        if stop_station not in results:
            results[stop_station] = (0, 0)
        results[start_station] = (results[start_station][0] + start_count, results[start_station][1])
        results[stop_station] = (results[stop_station][0], results[stop_station][1] + stop_count)
    for station in sorted(results.keys()):
        (start_count, stop_count) = results[station]
        my_output_stream.write(f"{station}\t({start_count}, {stop_count})\n")



# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    my_mapper_input_parameters = [(1, 0), (0, 1)]
    
    # 2. We call to my_map
    my_map(my_input_stream,
           my_output_stream,
           my_mapper_input_parameters
    )

