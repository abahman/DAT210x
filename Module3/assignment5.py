import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
#
df = pd.read_csv('/Users/ammarbahman/desktop/dat210x/module3/Datasets/wheat.data',sep =',')


#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
#
df = df.drop(labels=['id'],axis =1)
df = df.drop(labels=['area'],axis =1)
df = df.drop(labels=['perimeter'],axis =1)


#
# TODO: Plot a andrew curve chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
#
plt.figure()
andrews_curves(df, 'wheat_type',alpha =0.4)



plt.show()


