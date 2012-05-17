import math, random, sys, csv
from utils import parse, print_evaluation 
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
"""

if __name__ == '__main__':
    filename = 'data/jester-data-1.csv'
    items = {}
    users = {}
    matrix = []

    matrix, users, items = parse(filename)
    f = Filter(matrix, users, items)

    if len(sys.argv) == 3:
        method = sys.argv[1]
        testFile = sys.argv[2]
        testData = csv.reader(open(testFile, "r"))
        results = f.execute(method, testData)
        print_evaluation(f, method, results)
    elif len(sys.argv) == 2 and sys.argv[1] == 'all':
        method = "adj_weighted_sum"
        testData1 = csv.reader(open("data/TestSet01.csv", "r"))
        testData2 = csv.reader(open("data/TestSet02.csv", "r"))
        testData3 = csv.reader(open("data/TestSet03.csv", "r"))
        testData4 = csv.reader(open("data/TestSet04.csv", "r"))

        results1 = f.execute(method, testData1)
        results2 = f.execute(method, testData2)
        results3 = f.execute(method, testData3)
        results4 = f.execute(method, testData4)
        
        print_evaluation(f, "TestSet01", results1)
        print_evaluation(f, "TestSet02", results2)
        print_evaluation(f, "TestSet03", results3)
        print_evaluation(f, "TestSet04", results4)
    else:
        print 'Expected input format: python EvaluateCFList.py <method> <testList>'
