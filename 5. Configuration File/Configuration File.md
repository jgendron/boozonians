# Alien-nation Configuration File

## Category

*Alien-nation is data classification challenge.  You will use 21 features to conduct a binary classification of aliens as either friendly or dangerous.

## Relevant files and paths

*Problem Text.md – This file is the background for alien-nation, please read before beginning.
*alien_train.csv – This file is the training data set.  Each field represents one feature of the alien (columns B to V).  You will you use this data in conjunction with the results (column A) to train your model.
*alien_test.csv – This file is the test data set.  Once your model is trained run the model against this set and provide the answers to your administrator.  You will notice in this model there is no answer column, the features are instead located in columns A to U.
*alien_answer_key.txt – This file is the answer key for the test set.  It is a sequential text file with each result (friendly or dangerous) separated by a newline character.  It will be available to proctors only until the end of the exam!
*scorer.py - This script scores the solutions submitted by students after taking a sequential text file of solutions (“friendly” or “dangerous” separated by newline). It will be available only to proctors.
*SolutionApproach.Rproj – This file contains several models which solve the classification problem to varying degrees of accuracy.  The file will be available to students once the completion is over.

## Total Points
There are a total 2,437 aliens to classify.  You will receive one point for each alien correctly classified as friendly or hostile.  There is no differentiation I points for false positives versus false negatives.

## Hints
See next page.  Do not go here until you have tried your own algorithms.
















Conduct a search on classification models which are able to take advantage of large features with discrete and continues variables.  Here are some algorithms that were used with varying degrees of success while designing the problem:

*Naïve Bayes
*Classification Tree
*Conditional Inference Tree
*Random Forest

Good luck, the future of Earth depends on you!

