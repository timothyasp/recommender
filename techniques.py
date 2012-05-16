import math
import numpy

"""
    Collection of collaborative filtering techniques:
"""

class Filter:

    def __init__(self, matrix, users, items):
        self.matrix = matrix
        self.users = users
        self.items = items

    def execute(self, method, tests):
        length = 0
        results = []
        print "Technique: "+method
        print "userID, itemID, Actual_Rating, Predicted_rating, Delta_Rating"
        for row in tests:
            if len(row) > 1:
                userID = int(row[0])
                itemID = int(row[1])
                rating = float(self.users.get(userID)['ratings'][itemID])
                if rating != 99:
                    if method == 'weighted_sum':
                        predicted = self.weighted_sum(userID, itemID, 
                                                      "pearson", False)
                    elif method == 'adj_weighted_sum':
                        predicted = self.weighted_sum(userID, itemID, 
                                                      "pearson", True)
                    elif method == 'cosine_weighted_sum':
                        predicted = self.weighted_sum(userID, itemID,
                                                      "cosine", False)
                    elif method == 'cosine_adj_weighted_sum':
                        predicted = self.weighted_sum(userID, itemID,
                                                      "cosine", True)
                    elif method == 'default_voting':
                        predicted = self.weighted_sum(userID, itemID,
                                                      "default_voting", True)
                    else:
                        print "Method not supported... Exiting."
                        return
                    print userID,",",itemID,",",rating,",",predicted,",",(rating-predicted)
                    results.append({'predicted': predicted, 'actual': rating})
                    length += 1
        print 
        return results

    def mean_absolute_error(self, results):
        return sum([abs(x['predicted'] - x['actual']) for x in results])/len(results)

    def mean_squared_error(self, results):
        return sum([pow((x['predicted'] - x['actual']), 2) for x in results])/len(results)

    def root_mean_squared_error(self, results):
        return self.mean_squared_error(results)**.5

    def normalized_mean_absolute_error(self, results):
        rmax = 10
        rmin = -10
        return self.mean_absolute_error(results)/(rmax - rmin)

    def weighted_sum(self, userID, itemID, method, is_adjusted):
        absSim = simSum = 0
        userx = self.users.get(userID)
        avg_rating = userx['avg_rating']

        for uIDy, usery in self.users.iteritems():
            itemVal = float(usery['ratings'][itemID])
            if userID != uIDy and itemVal != 99:
                if method == 'default_voting':
                    sim = self.default_voting(userx['ratings'],
                                              usery['ratings'], itemID)
                else: 
                    sim = self.sim(method, userx['ratings'], usery['ratings'])
                absSim += abs(sim)
                if not is_adjusted:
                    simSum += sim * float(itemVal)
                else: 
                    simSum += sim * (float(itemVal) - avg_rating)
                    
        k = 1 / absSim
        if not is_adjusted:
            return k*simSum
        else:
            return avg_rating+k*simSum

    """ 
        Pearson Correlation used as similarity between two vectors
    """
    def sim(self, method, x, y):
        if method == 'cosine':
            return self.cosine(x, y)
        elif method == 'pearson':
            return self.pearson(x, y)
        elif method == 'default_voting':
            return self.default_voting(x, y)
        else:
            print "Similarity Method not supported"

    def cosine(self, u, v):
        return numpy.dot(u, v) / (math.sqrt(numpy.dot(u, u)) * math.sqrt(numpy.dot(v, v))) 

    def default_voting(self, x, y, item):
        d = self.items[item].get('avg')
        n = sumx = sumy = sumxSq = sumySq = prodSum = 0

        #regular sums
        for i in xrange(len(x)): 
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

        #do pearson score 
        num = prodSum - (sumx*sumy / n)
        den = math.sqrt((sumxSq - sumx**2 / n) * (sumySq - sumy**2 / n))

        if den == 0: return 1
        return num/den
        

    def pearson(self, x, y):
        n = sumx = sumy = sumxSq = sumySq = prodSum = 0

#regular sums
        for i in xrange(len(x)): 
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

#do pearson score 
        num = prodSum - (sumx*sumy / n)
        den = math.sqrt((sumxSq - sumx**2 / n) * (sumySq - sumy**2 / n))

        if den == 0: return 1
        return num/den

