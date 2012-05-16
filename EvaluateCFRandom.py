import math, random, sys
from utils import parse, process
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

def gen_tests(data, size):
    tests = []
    for i in xrange(size):
        uid = random.randint(0, len(data)-1)
        iid = random.randint(0, len(data[uid]['ratings'])-1)
        if float(data[uid]['ratings'][iid]) != 99:
            tests.append([uid,iid])
        else:
            tests.append([uid,random.randint(0, len(data[uid]['ratings'])-1)])

    return tests

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Expected input format: python EvaluateCFList.py <method> <testList>'
    else:
        filename = 'data/jester-data-1.csv'
        users = {}
        matrix = []

        size = int(sys.argv[2])

        matrix, users = parse(filename)
        testData = gen_tests(users, size)
        f = Filter(matrix, users)

        method = sys.argv[1]
        if method == 'all':
            w_results = f.execute('weighted_sum', testData)
            a_w_results = f.execute('adj_weighted_sum', testData)
            c_w_results = f.execute('cosine_weighted_sum', testData)
            c_a_w_results = f.execute('cosine_adj_weighted_sum', testData)
            print "Weighted Sum MAE: ",f.mean_absolute_error(w_results)
            print "Adjusted Weighted Sum MAE: ",f.mean_absolute_error(a_w_results)
            print "Cosine Weighted Sum MAE: ",f.mean_absolute_error(c_w_results)
            print "Cosine Adjusted Weighted Sum MAE: ",f.mean_absolute_error(c_a_w_results)
        else:
            results = f.execute(method, testData)

            print "MAE: ",f.mean_absolute_error(results)
            #print "MSE: ",f.mean_squared_error(results)
            #print "RMSE: ",f.mean_squared_error(results)

