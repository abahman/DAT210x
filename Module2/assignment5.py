import pandas as pd
import numpy as np


# TODO:
# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan
#
header_title = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
df = pd.read_csv('/Users/ammarbahman/desktop/dat210x/module2/Datasets/census.data',sep =',',names=header_title)

print df.head(n=3) # see the first n rows including the head
print ' '
# TODO:
# Figure out which features should be continuous + numeric
# Convert these to the appropriate data type as needed,
# that is, float64 or int64
#
print df.dtypes
print ' '

# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal types using
# the method discussed in the chapter.
#method 1
ordered_class = ['<=50K', '>50K']
df['class1'] = df['classification'].astype("category",
                                             ordered=True,
                                             categories=ordered_class
                                             ).cat.codes

#method 2
df['class2'] = df['classification'].astype("category").cat.codes
df['class3'] = df['education'].astype("category").cat.codes
df['class4'] = df['sex'].astype("category").cat.codes


# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
#
df['class5'] = df['race'].astype("category").cat.codes

# TODO:
# Print out your dataframe
print df