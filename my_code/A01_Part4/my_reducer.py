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
import datetime
import json


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    """
        This function reads lines from my_input_stream, formats them as required, and writes them to my_output_stream.

    Args:
        - my_input_stream: A file-like object for reading input data.
        - my_output_stream: A file-like object for writing output data.
        - my_reducer_input_parameters: Additional parameters to be used in the reducer.

    Returns:
        - None
    """
    count = 0
    for line in my_input_stream:
        key_value = line.strip().split("\t")
        if key_value[0] == "universal":
            trip = dict(zip(('start_time', 'stop_time', 'start_station_name', 'stop_station_name'), key_value[1].strip('()').split(" @ ")))
            my_output_stream.write(
                "By_Truck\t({}, {}, {}, {})\n".format(
                    datetime.datetime.strptime(trip['start_time'], '%Y/%m/%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S'),
                    trip['start_station_name'],
                    datetime.datetime.strptime(trip['stop_time'], '%Y/%m/%d %H:%M:%S').strftime('%Y/%m/%d %H:%M:%S'),
                    trip['stop_station_name']
                )
            )
            count += 1
            
    if count == 1:
        print(f"'{count}' entry written to '{my_output_stream.name}'")
    else:
        print(f"'{count}' entries written to '{my_output_stream.name}'")



    

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

