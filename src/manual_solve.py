#!/usr/bin/python

import os, sys
import json
import numpy as np
import re
import time
from collections import Counter

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.


# Written by Thomas below this comment
def solve_5582e5ca(x):
    shape = x.shape
    value = Counter(x.flatten()).most_common(1)
    x = np.full(shape=shape, fill_value=(value[0][0]))
    return x

def solve_d511f180(x):
    shape = x.shape
    for row in range(shape[0]):
        for column in range(shape[1]):
            if x[row][column] == 8:
                x[row][column]=5
            elif x[row][column] == 5:
                x[row][column]=8
    return x

def solve_f8b3ba0a(x):
    x_non_zero = (x[(x!=0)])
    value = Counter(x_non_zero.flatten()).most_common()
    #Thomas: Applied fix for incorrect shape error by removing extra brackets
    #that were included for each element of the matrix. Also vecotirixed it by
    # adding extra brackets the beginning and end of np.arrray 
    x = np.array([[value[-3][0]],
                 [value[-2][0]],
                 [value[-1][0]]])
    return x
# Written by Thomas above this comment

# Written by Dave below this line
def solve_f8ff0b80(x):
    x_non_zero = (x[(x!=0)])
    value = Counter(x_non_zero.flatten()).most_common(3)
    #Thomas: Applied fix for incorrect shape error by removing extra brackets
    #Thomas: Removed non xero values as well before finding most common
    #that were included for each element of the matrix. Also vecotirixed it by
    # adding extra brackets the beginning and end of np.arrray 
    x = np.array([[value[0][0]],
                  [value[1][0]],
                  [value[2][0]]])
    return x

def solve_c8f0f002(x):
    shape = x.shape
    for row in range(shape[0]):
        for column in range(shape[1]):
            if x[row][column] == 7:
                x[row][column]= 5
            elif x[row][column] == 5:
                x[row][column]= 7
    return x

def solve_d631b094(x):
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
     #Thomas: function above was not running because of typo error -> not including 'd'
     # in function name
     #Correction: renamed from np.nonzero to check if value !=0
     value = Counter((x[(x!=0)]).flatten()).most_common(1)
     x = np.full(shape=(1,value[0][1]), fill_value=(value[0][0]))
     return x

# Uses Depth-First-Search to identify the number of discrete objects (shapes) within the grid
# keeps track of each space in rows/columns scanned 
# returns the number of discrete objects which is used as a parameter to shape the size of the 
# output grid (numpy array) the output design is filled diagonally 
# ARC task number: d0f5fe59.json 

def solve_d0f5fe59(x):
    Matrix = x 
    #shape = x.shape
    row = len(Matrix)
    col = len(Matrix[0])    
    #x = Matrix(row, col, x) 
    print(x)
    class Matrix:
        def __init__(self, row, col, x):
            self.Row = row
            self.Col = col
            self.matrix = x
        
        # fx checks if a square can be included in the DFS, 
        # checks rows/cols values 1 and above
        # and has not been scanned 
        def isSafe(self, i, j, scan):
            return (i >=0 and i < self.Row and
                   j >=0 and j <self.Col and not 
                   scan[i][j] and self.matrix[i][j])
        
        # checks the neighbouring 8 squares 
        def DFS(self, i, j, scan):
            # get row / col nums of adjacent squares 
            rowNumr = [-1,-1, -1, 0, 0, 1, 1, 1];
            colNumr = [-1, 0, 1, -1, 1, -1, 0, -1];
            scan[i][j] = True # square has been scanned 
            # recursively check neighbours
            for k in range(8):
                if self.isSafe(i + rowNumr[k], j + colNumr[k], scan):
                    self.DFS(i + rowNumr[k], j + colNumr[k], scan)
        
        # returns count of descrete object shapes in grid
        # passes the count as a parameter to an output grid (numpy array)
        # fills the output grid(new_array) with output shape 
        def discreteObj(self):
            # intialise a boolean array for scanned sqaures, initialise to False
            scan =[[False for j in range(self.Col)] for i in range(self.Row)]
            count = 0 
            # traverse across the matrix 
            for i in range(self.Row):
                for j in range(self.Col):
                    # if a square greater than zero not yet scanned it is a new discrete object 
                    if scan[i][j] == False and self.matrix[i][j] > 0:
                        self.DFS(i, j, scan)
                        # increment the count of discrete objects (and new_array size)
                        count += 1
                        # count is used as parameter to shape the size of output array
                        x = np.ones((count, count), dtype=int)
                        # fill design on the diagonals with colour blue(8)
                        np.fill_diagonal(x, 8)
                        
            return x
=======
>>>>>>> Stashed changes
      #Thomas: function above was not running because of typo error -> not including 'd'
      # in function name
      #Correction: renamed from np.nonzero to check if value !=0
      value = Counter((x[(x!=0)]).flatten()).most_common(1)
      x = np.full(shape=(1,value[0][1]), fill_value=(value[0][0]))
      return x
<<<<<<< Updated upstream
=======
>>>>>>> 128304b0405838856fb9c3e9725dee9801657817
>>>>>>> Stashed changes
# Written by Dave above this line

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))

if __name__ == "__main__": main()

