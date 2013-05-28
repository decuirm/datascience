"""
Matt Decuir, Spring 2013
Intro to Data Science, Assignment 3

Implements a relational join as a MapReduce query 
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #key = order_id
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    order = []
    lineitemlist = []
    for list in list_of_values:
      if list[0] == 'order':
        order.append(list)
      elif list[0] == 'line_item':
        lineitemlist.append(list)

    for line in lineitemlist:
      mr.emit(order[0]+line)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
