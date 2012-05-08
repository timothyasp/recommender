import math, random

"""
   Wrapper around the User-Specified test. Takes as input a list of (userID,
   itemID) pairs and does the following:
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
