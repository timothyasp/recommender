import math, random, sys, csv
from utils import parse, process
from techniques import Filter

"""
   Wrapper around the User-Specified test. Takes as input a list of
   (userID, itemID) pairs and does the following:
       - For each test case pair, determine whether it is valid, ie whether
         rating(userID, itemID) != 99 and compute the predicted rating 
       - Compare the predicted rating with the actual rating
       - Output the result
       - Compute the Mean Absolute Error (MAE)

    Inputs: method, filename 
        - method: ID of the collaborative filtering method to be used
        - filename: name of the file containing the list of test cases
            - format: (UserID, ItemID)
"""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Expected input format: python EvaluateCFList.py <method> <testList>'
    else:
        method = sys.argv[1]
        testFile = sys.argv[2]
        testData = csv.reader(open(testFile, "r"))

        filename = 'data/jester-data-1.csv'
        items = users = {}
        matrix = []
        matrix, users, items = parse(filename)

        f = Filter(matrix, users, items)
        f.execute(method, testData)


