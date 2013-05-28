"""
Matt Decuir, Spring 2013
Intro to Data Science, Assignment 3

Trims the last 10 characters of a string and returns only unique results using a MapReduce Query
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    value = record[1][0:-10]
    mr.emit_intermediate(value,1)

def reducer(key, list_of_values):
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
