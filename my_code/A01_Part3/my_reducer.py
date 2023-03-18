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
import codecs


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def process_line(line):
    fields = line.strip().split("\t")
    station_name = fields[0]
    start_count, stop_count = map(int, fields[1][1:-1].split(", "))
    return station_name, (start_count, stop_count)

def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters=None):
    results = {}
    for line in my_input_stream:
        station, (start_count, stop_count) = process_line(line)
        if station not in results:
            results[station] = (0, 0)
        results[station] = (results[station][0] + start_count, results[station][1] + stop_count)
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
    # 1. We collect the input values
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    my_reducer_input_parameters = []

    # 5. We call to my_reduce
    my_reduce(my_input_stream,
              my_output_stream,
              my_reducer_input_parameters
             )

