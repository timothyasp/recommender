import math, random
from utils import parse, process

"""
    A wrapper around the random sampling evaluation technique which performs the
    following:
    - Randomly generates a `size` number of test cases such that the rating (userID,
      itemID) != 99 (ie each test case represents prediction of a score actually
      found in the matrix).
    - For each generated test case, use the selected collborative filtering method
      to predict the rating. 
    - Compare the predicted rating with the actual rating
    - Output the results
    - Compute the output of the Mean Absolute Error (MAE) achieved in your test

    Inputs: method, size
        - method: Collaborative filtering method to use
        - size: number of test cases to generate
"""

if __name__ == '__main__':
    filename = 'data/jester-data-1.csv'
    """
        items[itemID] = { 'val': total value of rankings, 
    """
    items = users = {}
    matrix = []
    matrix, users, items = parse(filename)

