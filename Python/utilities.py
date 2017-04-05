# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:53:24 2017

@author: hangzh
"""

# This file contains a set of functions that can be useful in data science work
import sys

def report_progress(current_index, max_index, report_interval, previous_status=None):
    # current_index: current index in the for loop
    # max_index: the largest index in the for loop
    # report_interval: how often do you want to print out the progress. 5 means every 5% prints out a percentage on the screen. 
    # Otherwise, any change in percentage prints out a dot on the screen
    # previous_status: print the current percentage, which can be the input of calling this function
    percent = int(current_index * 100 / float(max_index))
    if previous_status != percent:
        if percent % report_interval == 0:
          sys.stdout.write("%s%%" % percent)
          sys.stdout.flush()
        else:
          sys.stdout.write(".")
          sys.stdout.flush()

        previous_status = percent
    return previous_status