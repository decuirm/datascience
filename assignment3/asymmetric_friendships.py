"""
Matt Decuir, Spring 2013
Intro to Data Science, Assignment 3

Counts the number of asymmetric friendships using a MapReduce Query
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    friend1 = record[0]
    friend2 = record[1]
    mr.emit_intermediate(friend1,friend2)
    mr.emit_intermediate(friend2,friend1)

def reducer(key, list_of_values):
    for name in list_of_values:
        if list_of_values.count(name) <2:
            mr.emit((key,name))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
