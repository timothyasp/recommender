import math
"""
    Collection of collaborative filtering techniques:
"""

class Filter:

    def __init__(self, matrix, users, items):
        print "Initiailized Filtering class"
        self.matrix = matrix
        self.users = users
        self.items = items

    def weighted_sum(self):
        print "Starting weighted sum: "
        for userID, user in self.users.iteritems():
            print userID, ": ", user

    """ 
        Pearson Correlation used as similarity between two vectors
    """
    def sim(self, x, y):
        return self.pearson(x, y)

    def pearson(self, x, y):
        n=len(x)
        vals=range(n)

#regular sums
        sumx=sum([float(x[i]) for i in vals])
        sumy=sum([float(y[i]) for i in vals])

#sum of the squares
        sumxSq=sum([x[i]**2.0 for i in vals])
        sumySq=sum([y[i]**2.0 for i in vals])

#sum of the products
        pSum=sum([x[i]*y[i] for i in vals])

#do pearson score 
        num=pSum-(sumx*sumy/n)
        den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2))**.5)

        if den == 0: return 1
        r=num/den
        return r

