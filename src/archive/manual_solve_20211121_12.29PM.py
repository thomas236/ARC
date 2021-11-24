#!/usr/bin/python
"""NUI Galway CT5132/CT5148 Programming and Tools for AI (James McDermott)

Assignment 3: Hand-coding solutions for the Abstraction and Reasoning Corpus
Student name(s): Thomas Sebastian, David Power
Student ID(s): 21250103,

Github URLs:
Thomas Sebastian --> https://github.com/thomas236/ARC
David Power -->
"""

import os, sys
import json
import numpy as np
import re
import time
from collections import Counter
from skimage import measure


### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

def solve_5582e5ca(x):
    '''
    Solves task 5582e5ca.
    The input train array is converted/flattened into a 1D array and the 
    most common color in the 1D array is stored into variable, value.
    A 2D numpy array is created that is polulated with the most common color. 
    This 2D array is the solution and is retßurned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    value = Counter(x.flatten()).most_common(1)
    x = np.full(shape=shape, fill_value=(value[0][0]))
    return x

def solve_d511f180(x):
    '''
    Solves task d511f180.
    The input train array is scanned by row and column. Each element is
    searched for color code '8' and '5' in sequence. If the value is found,
    the value in the numpy array is flipped for '5' and 8 respectively.
    This 2D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    for row in range(shape[0]):
        for column in range(shape[1]):
            if x[row][column] == 8:
                x[row][column]=5
            elif x[row][column] == 5:
                x[row][column]=8
    return x

def solve_f8b3ba0a(x):
    '''
    Solves task f8b3ba0a.
    The input train array if filtered for non zero values. The 3 least common
    values of this resulting array is used to construct a vector with 3 rows.
    This 2D array vector is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    x_non_zero = (x[(x!=0)])
    value = Counter(x_non_zero.flatten()).most_common()
    x = np.array([[value[-3][0]],
                  [value[-2][0]],
                  [value[-1][0]]])
    return x

def solve_22eb0ac0(x):
    '''
    Solves task 22eb0ac0.
    Each row in the input 2D array is scanned for the same color in first
    and last column. Color code '0' is ignored.
    All columns in the row is filled with the same color if the first
    and last color are found to be same.
    This 2D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    for row in range(shape[0]):
        if x[row][0]!=0:
            if x[row][0] == x[row][shape[1]-1]:
                for column in range(1,shape[1]-1):
                    x[row][column]=x[row][0]
    return x

def solve_e3497940(x):
    '''
    Solves task e3497940.
    The 2D input array is sliced into 2 halves vertically.
    Values in the right slice is mirrored into first slice for those elements
    that are coded with original color code = 0.
    This resulting left 2D array array slice is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    for row in range(shape[0]):
        for column in range (int(shape[1]/2)):
            if x[row][column]==0:
                x[row][column] = x[row][shape[1]-column-1]
    x = x[:,:4]
    return x

def solve_c3f564a4(x):
    '''
    Solves task c3f564a4.
    A dictionary is creacted to keep track of color codes in reverse order.
    that are present after a sepecific color. For this step, color code
    '0' is ignored.
    The 2D array is scanned from right to left and top to bottom. If color
    code '0' is found, that value is replaced by value in the dictionary
    (discussed above) to fill in the specific location in the 2D array.
    To genralise this apprach, another dictionary is alse created to keep
    track of color codes before a specific color.
    Similar to approach above, the 2D array is scanned from left to right 
    and top to bottom are filled when '0' is found. This generalisation step
    takes care of edge cases where '0' is found in left and right most columns.
    
    This 2D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    reverse_pattern = {}
    for row in range(shape[0]):
        for column in range (shape[1]-1,0,-1):
            if x[row][column]!=0:
                reverse_pattern.update({x[row][column]:x[row][column-1]})
    for row in range(shape[0]):
        for column in range(shape[1]-1,-1,-1):
            if x[row][column]==0:
                x[row][column]=reverse_pattern.get(x[row][column+1])
    
    forward_pattern = {}
    for row in range(shape[0]):
        for column in range (0,shape[1]-1):
            if x[row][column]!=0:
                forward_pattern.update({x[row][column]:x[row][column+1]})
    for row in range(shape[0]):
        for column in range(shape[1]):
            if x[row][column]==0:
                x[row][column]=forward_pattern.get(x[row][column-1])
    return x


def solve_f8ff0b80(x):
    '''
    Solves task f8ff0b80.
    The 2D input array is filtered for non zero values. 3 most common
    non zero color code are used to constructed a 3 row vector.
    This 2D array vector is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    x_non_zero = (x[(x!=0)])
    value = Counter(x_non_zero.flatten()).most_common(3)
    x = np.array([[value[0][0]],
                  [value[1][0]],
                  [value[2][0]]])
    return x

def solve_c8f0f002(x):
    '''
    Solves task c8f0f002.
    The input train array is scanned by row and column. Each element is
    searched for color code '7' and '5' in sequence. If the value is found,
    the value in the numpy array is flipped for '5' and 7 respectively.
    This 2D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    shape = x.shape
    for row in range(shape[0]):
        for column in range(shape[1]):
            if x[row][column] == 7:
                x[row][column]= 5
            elif x[row][column] == 5:
                x[row][column]= 7
    return x

def solve_d631b094(x):
    '''
    Solves task d631b094.
    The input train array is filtered for nonzero values. The 2D array is then
    flattened and the most common value is used to create an array with the 
    dimensions as the number of most common color code. The 2D array is filled
    with this most common collor code.
    This 1D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 1D Numpy integer array of same dimensions as the input array.
    '''
    value = Counter((x[(x!=0)]).flatten()).most_common(1)
    x = np.full(shape=(1,value[0][1]), fill_value=(value[0][0]))
    return x


def solve_d0f5fe59(x):
    '''
    Solves task d0f5fe59.
    The input train array is filtered for nonzero values. The 2D array is then
    flattened and the most common value is found, which is the color of the
    object. Using Skimage's 'find_cotours' function,
    the number of obects are detected. An identity matrix is created with the 
    same number of dimensions as the number of objects. This identity matrix
    is then transposed and diagonal mutiplied by the color of the object.
    This 2D array is the solution and is returned.
    Parameters:
    x: 2D Numpy integer array, a single grid containing color codes
    specific to this task
    Returns:
    x: 2D Numpy integer array of same dimensions as the input array.
    '''
    x_non_zero = (x[(x!=0)])
    most_common = Counter(x_non_zero.flatten()).most_common()
    contours = measure.find_contours(x)
    x=np.identity(len(contours), dtype="int")
    x=most_common[0][0]*x.T
    return x
  
  
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
            # if the name fits the reverse_pattern eg solve_abcd1234
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

