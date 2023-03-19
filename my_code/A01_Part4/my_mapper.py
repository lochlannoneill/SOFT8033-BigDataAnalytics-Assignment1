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


# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    res = {}
    fields = line.strip().split(",")
    if len(fields) == 16:
        res["start_time"] = datetime.datetime.strptime(fields[0], "%Y/%m/%d %H:%M:%S")
        res["stop_time"] = datetime.datetime.strptime(fields[1], "%Y/%m/%d %H:%M:%S")
        res["start_station_id"] = int(fields[3])
        res["start_station_name"] = fields[4]
        res["stop_station_id"] = int(fields[7])
        res["stop_station_name"] = fields[8]
        res["bike_id"] = int(fields[11])
    return res

def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    for line in my_input_stream:
        trip = process_line(line)
        # print('my_mapper <var: trip> == ', trip)
        if trip["bike_id"] == my_mapper_input_parameters[0]:
            my_output_stream.write("universal\t({} @ {} @ {} @ {})\n".format(trip['start_time'], trip['stop_time'], trip['start_station_name'], trip['stop_station_name']))


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
    BIKE_ID = 35143
    my_mapper_input_parameters = [ BIKE_ID ]  # TODO - take as paramter from my_meta-alogorithm.py

    # 2. We call to my_map
    my_map(my_input_stream,
           my_output_stream,
           my_mapper_input_parameters
          )

