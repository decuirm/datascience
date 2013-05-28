"""
Matt Decuir, Spring 2013
Intro to Data Science, Assignment 3

Matrix multiplication using a MapReduce Query
"""

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # for each a record, output key = (row, col) and value = (matrix,row,col, val)
    # plus output key for every other row/col where this number will be used
    matrix = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if matrix == 'a':
	    for i in range(0,5):
	    	mr.emit_intermediate((row,i),(matrix,row,col,val))
    if matrix == 'b':
    	for j in range(0,5):
    		mr.emit_intermediate((j, col),(matrix,row,col,val))

def reducer(key, list_of_values):
	# for each item in a, multiply a's value (row/col) by b's value (col/row)
	# 	add value to sum
	# output sum

	#split values into dicts a and b
	a = {}
	b = {}
	for list in list_of_values:
		if list[0] == 'a':
			a[list[1],list[2]] = list[3]
		elif list[0] == 'b':
			b[list[1],list[2]] = list[3]

	#calculate matrix multiplication value of cell
	row = key[0]
	col = key[1]
	sum = 0
	aval = 0
	bval = 0
	for i in range(0,5):
		if (row,i) in a:
			aval = a[row,i]
		else:
			aval = 0
		if (i,col) in b:
			bval = b[i,col]
		else:
			bval = 0
		sum += aval * bval
	mr.emit((row,col,sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
