# Alien-nation Configuration File

## Category

Alien-nation is a data classification challenge. Teams will use 21 features to conduct a binary classification of aliens as either friendly or dangerous.

## Relevant files and paths

* Problem Text.md – This file is the background for alien-nation, please have all teams read before beginning.

* alien_train.csv – This file is the training data set. Each field represents one feature of the alien (columns B to V). Teams will use this data in conjunction with the results (column A) to train their model.

* alien_test.csv – This file is the test data set. Once a team has trained its model, have them run the model against this set and then provide the answers to the administrator. You will notice in this dataset there is no answer column, the features are instead located in columns A to U.

* alien_answer_key.txt – This file is the answer key for the test set. It is a sequential text file with each result (friendly or dangerous) separated by a newline character. It will be available only to proctors until the end of the exam. Do not disseminate to teams.

* scorer.py - This script scores the solutions submitted by students after taking a sequential text file of solutions (“friendly” or “dangerous” separated by newline). It will be available only to proctors. Do not disseminate to teams.

* slides-final.Rmd – This file contains redproducible models which solve the classification problem to varying degrees of accuracy. Make this file available to students once the hackathon is over.

## Total Points
There are a total 2,437 aliens to classify. A team will receive one point for each alien correctly classified as friendly or hostile. There is no differentiation of points for false positives versus false negatives.

## Hints
See below. Do not provide access to teams until they have tried their own algorithms.

* Have teams conduct a search on classification models which are able to take advantage of large features with categorical variables.

* Common sense is useful in this problem. The aliens are physical creatures and they the friendly and dangerous have characteristics that are intuitive in some cases. For instance, in a business example, you can tell a bit about someone by how they dress. You can take these approaches with this data as well.

* The datasets are failrly balanced. What does that permit in terms of modeling?

* Have you explored the data visual and graphically? You would be amazed at how many trends are visible by simple cross-tabs (even in Excel).

* Because this data is categorical, linear regression is not as useful. What types of models are good for categorical indicators? (A: Classification Trees, Conditional Inference Trees, and Random Forest)



Good luck to your students, the future of Earth depends on them!