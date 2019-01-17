import pandas
import numpy
import random

# RV of pandas.read_csv are DataFrames
train = pandas.read_csv('~/repos/kaggle/titanic/input/train.csv')
test = pandas.read_csv('~/repos/kaggle/titanic/input/test.csv')

print(train.shape)
print(test.shape)