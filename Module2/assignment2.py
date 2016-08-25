import pandas as pd


# TODO: Load up the 'tutorial.csv' dataset
#
df = pd.read_csv('/Users/ammarbahman/desktop/dat210x/module2/Datasets/tutorial.csv',sep =',')
print df
print ' '

# TODO: Print the results of the .describe() method
#
print df.describe()
print ' '


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
print df.loc[2:4, 'col3']
print ' '

