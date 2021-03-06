import math, random, sys
from utils import parse, print_evaluation
from techniques import Filter

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

def get_ratings(data, userID):
    return data[userID]['ratings']

def get_val(data, userID, itemID):
    return float(get_ratings(data, userID)[itemID])

def gen_tests(data, size):
    tests = []
    for i in xrange(size):
        uid = random.randint(0, len(data)-1)
        iid = random.randint(0, len(get_ratings(data, uid))-1)
        while get_val(data, uid, iid) == 99:
            iid = random.randint(0, len(get_ratings(data, uid))-1)

        tests.append([uid,iid])

    return tests

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Expected input format: python EvaluateCFList.py <method> <testList>'
    else:
        filename = 'data/jester-data-1.csv'
        items = {}
        users = {}
        matrix = []

        size = int(sys.argv[2])

        matrix, users, items = parse(filename)
        testData = gen_tests(users, size)
        f = Filter(matrix, users, items)

        method = sys.argv[1]
        print "Starting predictions"
        if method == 'all':
            w_results = f.execute('weighted_sum', testData)
            a_w_results = f.execute('adj_weighted_sum', testData)
            c_w_results = f.execute('cosine_weighted_sum', testData)
            c_a_w_results = f.execute('cosine_adj_weighted_sum', testData)
            print_evaluation(f, "Weighted Sum", w_results)
            print_evaluation(f, "Adjusted Weighted Sum", a_w_results)
            print_evaluation(f, "Cosine Weighted Sum", c_w_results)
            print_evaluation(f, "Cosine Adjusted Weighted Sum", c_a_w_results)
        else:
            results = f.execute(method, testData)
            print_evaluation(f, method, results)

