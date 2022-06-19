# Let’s say you work as a medical researcher.

# You are given a dataframe of patient data containing the age of the patient and two columns, smoking and cancer, indicating if the patient is a smoker or has cancer, respectively.

# Write a function, stratified_split, that splits the dataframe into train and test sets while preserving the approximate ratios for the values in a specified column (given by a col parameter).

# Note: Do not use scikit-learn.

# Example:

# Input:

# print(df)
# ...
#    age smoking cancer
# 0   25     yes    yes
# 1   32      no     no
# 2   10     yes     no
# 3   40     yes     no
# 4   75      no     no
# 5   80     yes     no
# 6   60     yes     no
# 7   60      no    yes
# 8   40     yes    yes
# 9   80     yes     no
# Output:

# def stratified_split(df, train_ratio=0.7, col='cancer') -> print(X_train)
# ...
#    age smoking cancer
# 8   40     yes    yes
# 6   60     yes     no
# 7   60      no    yes
# 4   75      no     no
# 9   80     yes     no
# 1   32      no     no
# 2   10     yes     no
# -----------------------
# print(X_test)
# ...
#    age smoking cancer
# 0   25     yes    yes
# 5   80     yes     no
# 3   40     yes     no

import pandas as pd
import numpy as np

def stratified_split(df, train_ratio , col):
    col_class_weights = (df[col].value_counts()/len(df)).to_dict()

    train_sample_count = (int)(len(df)* train_ratio)
    test_sample_count  = (int)(len(df) - train_sample_count)
    train_indexes = df.groupby(col, group_keys=False).apply(
        lambda x: x.sample(int(np.rint(train_sample_count * len(x) / len(df))))).sample(frac=1).index

    test_indexes = [i for i in df.index if i not in train_indexes]

    return df.loc[train_indexes], df.loc[test_indexes]



### Very elegant solution I found online for the same, username was annonymous so I don't know the real name.

def stratified_split(df, train_ratio , col):
    train, test = [], []
    df = df.sample(frac=1)
    for val in np.unique(df[col]):
        rows = int(round(len(df[df[col]==val]) * train_ratio))
        train.append(df[df[col]==val][0:rows])
        test.append(df[df[col]==val][rows:])
    return pd.concat(train), pd.concat(test)


  
