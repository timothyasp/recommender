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

    def execute(self, method, tests):
        for row in tests:
            if len(row) > 1:
                userID = int(row[0])
                itemID = int(row[1])
                rating = float(self.users.get(userID)['ratings'][itemID])
                if rating != 99:
                    print "userID: ",userID
                    print "itemID: ",itemID
                    print "User: ", self.users.get(userID)
                    if method == 'weighted_sum':
                        print "Estimated Rating: ",self.weighted_sum(userID, itemID)
                    else:
                        print "Method not supported... Exiting."
                        return
                    print "Actual Rating: ",rating
                    print "\n"


    def weighted_sum(self, userID, itemID):
        absSim = simSum = 0
        userx = self.users.get(userID)

        for uIDy, usery in self.users.iteritems():
            itemVal = float(usery['ratings'][itemID])
            if userID != uIDy and itemVal != 99:
                sim = self.sim(userx['ratings'], usery['ratings'])
                absSim += abs(sim)
                simSum += sim * float(itemVal)
                    
        k = 1 / absSim

        return k*simSum


    """ 
        Pearson Correlation used as similarity between two vectors
    """
    def sim(self, x, y):
        return self.pearson(x, y)

    def pearson(self, x, y):
        vals = range(len(x))
        n = sumx = sumy = sumxSq = sumySq = prodSum = 0

#regular sums
        for i in vals:
            xVal = float(x[i])
            yVal = float(y[i])
            if xVal != 99 and yVal != 99:
                """ Length counter of the number of pairs in pearson """
                n += 1
                sumx += xVal
                sumy += yVal
                sumxSq += xVal**2.0
                sumySq += yVal**2.0
                prodSum += xVal*yVal
                """print "sumx: ", sumx
                print "sumy: ", sumy
                print "sumxSq: ", sumxSq
                print "sumySq: ", sumySq
                print "prodSum: ", prodSum"""

#do pearson score 
        num = prodSum - (sumx*sumy / n)
        den = math.sqrt((sumxSq - sumx**2 / n) * (sumySq - sumy**2 / n))

        if den == 0: return 1
        return num/den

