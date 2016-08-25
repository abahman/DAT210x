import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/year/2015',header =1)[0]
#print df

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# see previous command line "header = 1"


# TODO: Get rid of any row that has at least 4 NANs in it
#
df = df.dropna(axis=0,thresh= 4)
#print df

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
df = df.drop([11,23,35],axis = 0) #[11,23,35] are the rows (index) that need to be deleted


# TODO: Get rid of the 'RK' column
#
df = df.drop(labels=['RK'],axis =1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop=True) # drop=True parameter tells Pandas not to keep a backup copy of the original index


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
print df.dtypes
print ' '
df.GP = pd.to_numeric(df.GP, errors='coerce') #errors='coerce' ensure that if the conversion not appicable, it converts to NaN
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df['+/-'] = pd.to_numeric(df['+/-'], errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df['PTS/G'] = pd.to_numeric(df['PTS/G'], errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')
df['G.1'] = pd.to_numeric(df['G.1'], errors='coerce')
df['A.1'] = pd.to_numeric(df['A.1'], errors='coerce')
df['G.2'] = pd.to_numeric(df['G.2'], errors='coerce')
df['A.2'] = pd.to_numeric(df['A.2'], errors='coerce')
print df.dtypes
print ' '

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
# to answer question 2:
print len(df['PCT'].unique())
