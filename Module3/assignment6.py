import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('/Users/ammarbahman/desktop/dat210x/module3/Datasets/wheat.data',sep =',')

#
# TODO: Drop the 'id' feature
# 
df = df.drop(labels=['id'],axis =1)


#
# TODO: Compute the correlation matrix of your dataframe
#
correlation = df.corr()
print correlation


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.figure()
plt.imshow(correlation, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()


