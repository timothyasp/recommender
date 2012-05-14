import sys, math, random, csv, types
from collections import defaultdict

"""
    Input format: 
        EvaluateCFRandom <method> <size>
            - method: Collaborative filtering method to use
            - size: number of test cases to generate

        EvaluateCFList <method> <filename>
            - method: ID of the collaborative filtering method to be used
            - filename: name of the file containing the list of test cases
                - format: (UserID, ItemID)

    Output format: 
        For each test case it prints a single line in the format below:
            userID, itemID, Actual_Rating, Predicted_Rating, Delta_Rating
            MAE Measure - printed at the end of the list

"""

def parse(filename):
    matrix = list()
    item_stats = {}
    user_stats = {}
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    for i, row in enumerate(reader):
        user_stats[i] = {'num': row[0], 'ratings': [col for col, x in enumerate(row[1:]) if float(x) != 99]}
        matrix.append(row[1:])
        for k, v in enumerate(row):
            if float(v) != 99 and k != 0:
# shift the dictionary key down one so it matches up with the values in user and
# matrix data 
                k = k-1
                if not item_stats.has_key(k): 
                    item_stats[k] = {'num': 0, 'avg': 0}
                else: 
                    val = item_stats[k]['avg']*item_stats[k]['num']
                    val += float(v)
                    item_stats[k]['num'] += 1
                    item_stats[k]['avg'] = val/item_stats[k]['num']

    return matrix, user_stats, item_stats

def process():
    print "process"


