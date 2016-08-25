import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#used in scatter 3D
from mpl_toolkits.mplot3d import Axes3D

#used in parallel coordinates
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates


#used in andrew's curve
from pandas.tools.plotting import andrews_curves

plt.style.use('ggplot') # Look Pretty
student_dataset = pd.read_csv("/Users/ammarbahman/desktop/dat210x/students.data", index_col=0)



my_series = student_dataset['G3']
my_dataframe = student_dataset[['G3', 'G2', 'G1']]

#histogram
my_series.plot.hist(alpha=0.5,cumulative=True,histtype='bar',bins=10)
my_dataframe.plot.hist(alpha=0.5,histtype='stepfilled')

#scatter 2D
student_dataset.plot.scatter(x='G1', y='G3')
plt.xlabel('G1')
plt.ylabel('G3')
plt.title('what studnets did in exam')


#scatter 3D
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(student_dataset['G1'], student_dataset['G3'], student_dataset['Dalc'], c='r', marker='.')



# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]

#Parallel Coordinates
plt.figure()
parallel_coordinates(df, 'target_names')


#andrew's curve
plt.figure()
andrews_curves(df, 'target_names')


#correlation and imshow()
df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
print df.corr()

plt.figure()
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()