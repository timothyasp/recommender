recommender
===========

Collaborative Filtering and Recommender Systems algorithm implementation 

Run Examples
============

```
   python EvaluateCFList.py weighted_sum data/TestSet01.csv
   python EvaluateCFList.py adj_weighted_sum data/TestSet01.csv
   python EvaluateCFList.py cosign_weighted_sum data/TestSet01.csv
   python EvaluateCFList.py cosign_adj_weighted_sum data/TestSet01.csv

   python EvaluateCFRandom.py weighted_sum 4
   python EvaluateCFRandom.py adj_weighted_sum 4
   python EvaluateCFRandom.py cosign_weighted_sum 4 
   python EvaluateCFRandom.py cosign_adj_weighted_sum 4
```

Or to run all the different filtering methods at once (with random test sets only) 
```
   python EvaluateCFRandom.py all 4
```
