# Ch.10 K-nearest Neighbors

## K-nearest Neighbors (KNN)

2 uses of KNN (from Wiki):

1. Classification - the output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors
2. Regression - the output is the property value for the object. This value is the average of the values of k nearest neighbors.

- With KNN, choosing the right features is very important.
- Case in point, for a recommendation system, you'll want:
  1. Features that directly correlate to the what you are trying to recommend
  2. Features that don't have a bias (ie. balanced sample)

## Distance formula

__Distance formula__ measures the distance between two vectors using the Pythagorean formula. 

- Smaller the number, the more similar they are.

![pythagorean formula](img/pyth_formula.png)

The formula can be expanded to multiple features.

![pythagorean formula large](img/pyth_formula_large.png)

Techniques
1. Normalizing - scaling different features
2. Weighting - weighing certain neighbors higher than others.


## Cosine similarity

__Cosine similarity__ compares the angles of the two vectors.



## Recap

- KNN is used for classification and regression and involves looking at the k-nearest neighbors.
- Classification = categorization into a group.
- Regression = predicting a response (like a number).
- Feature extraction means converting an item (like a fruit or a user) into a list of numbers that can be compared.
- Picking good features is an important part of a successful KNN algorithm.
