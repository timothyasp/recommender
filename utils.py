import sys, math, random, csv, types

"""
    Data format: 
        1. 3 Data ﬁles contain anonymous ratings data from 73,421 users.
        2. Data ﬁles are in .zip format, when unzipped, they are in Excel
           (.xls) format
        3. Ratings are real values ranging from -10.00 to +10.00 (the
           value "99" corresponds to "null" = "not rated").
        4. One row per user
        5. The ﬁrst column gives the number of jokes rated by that user.
           The next 100 columns give the ratings for jokes 01 - 100.
        6. The sub-matrix including only columns 5, 7, 8, 13, 15, 16, 17,
           18, 19, 20 is dense. Almost all users have rated those jokes
           (see discussion of "universal queries" in the above paper).
    (http://eigentaste.berkeley.edu/jester-data/jester-joke-texts.zip)

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

def parse(self, filename):
    reader = csv.reader(open(filename, 'r'), delimiter=',')

def process():
    print "process"
