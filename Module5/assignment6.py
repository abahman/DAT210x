import random, math
import pandas as pd
import numpy as np
import scipy.io

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import matplotlib

# If you'd like to try this lab with PCA instead of Isomap,
# as the dimensionality reduction technique:
Test_PCA = False

matplotlib.style.use('ggplot') # Look Pretty


def Plot2DBoundary(DTrain, LTrain, DTest, LTest):
  # The dots are training samples (img not drawn), and the pics are testing samples (images drawn)
  # Play around with the K values. This is very controlled dataset so it should be able to get perfect classification on testing entries
  # Play with the K for isomap, play with the K for neighbors. 

  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('Transformed Boundary, Image Space -> 2D')

  padding = 0.1   # Zoom out
  resolution = 1  # Don't get too detailed; smaller values (finer rez) will take longer to compute

  mesh_colors = ListedColormap(['#1e5ec4', '#41d973', '#ded587', '#e1d9d7'])
  plot_colors = ['blue','green','orange','red']

  # ------

  # Calculate the boundaries of the mesh grid. The mesh grid is
  # a standard grid (think graph paper), where each point will be
  # sent to the classifier (KNeighbors) to predict what class it
  # belongs to. This is why KNeighbors has to be trained against
  # 2D data, so we can produce this contour. Once we have the 
  # label for each point on the grid, we can color it appropriately
  # and plot it.
  x_min, x_max = DTrain[:, 0].min(), DTrain[:, 0].max()
  y_min, y_max = DTrain[:, 1].min(), DTrain[:, 1].max()
  x_range = x_max - x_min
  y_range = y_max - y_min
  x_min -= x_range * padding
  y_min -= y_range * padding
  x_max += x_range * padding
  y_max += y_range * padding

  # Using the boundaries, actually make the 2D Grid Matrix:
  xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution),
                       np.arange(y_min, y_max, resolution))

  # What class does the classifier say about each spot on the chart?
  # The values stored in the matrix are the predictions of the model
  # at said location:
  Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  # Plot the mesh grid as a filled contour plot:
  plt.contourf(xx, yy, Z, cmap=mesh_colors, z=-100)
  plt.axis('tight')

  # ------

  # When plotting the testing images, used to validate if the algorithm
  # is functioning correctly, size them as 5% of the overall chart size
  x_size = x_range * 0.05
  y_size = y_range * 0.05
  
  # First, plot the images in your TEST dataset
  img_num = 0
  for index in LTest.index:
    # DTest is a regular NDArray, so you'll iterate over that 1 at a time.
    x0, y0 = DTest[img_num,0]-x_size/2., DTest[img_num,1]-y_size/2.
    x1, y1 = DTest[img_num,0]+x_size/2., DTest[img_num,1]+y_size/2.

    # DTest = our images isomap-transformed into 2D. But we still want
    # to plot the original image, so we look to the original, untouched
    # dataset (at index) to get the pixels:
    img = df.iloc[index,:].reshape(num_pixels, num_pixels)
    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1), alpha=0.8)
    img_num += 1


  # Plot your TRAINING points as well... as points rather than as images
  for label in range(len(np.unique(LTrain))):
    indices = np.where(LTrain == label)
    ax.scatter(DTrain[indices, 0], DTrain[indices, 1], c=plot_colors[label], alpha=0.8, marker='o')

  # Plot
  plt.show()



#
# TODO: Use the same code from Module4/assignment4.py to load up the
# face_data.mat in a dataset called "df". Be sure to calculate the
# num_pixels value, and to rotate the images to being right-side-up
# instead of sideways. This was demonstrated in the M4/A4 code:
#
mat = scipy.io.loadmat('/Users/ammarbahman/desktop/dat210x/Module4/Datasets/face_data.mat')
df = pd.DataFrame(mat['images']).T
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))

# Rotate the pictures, so we don't have to crane our necks:
for i in range(num_images):
    df.loc[i,:] = df.loc[i,:].reshape(num_pixels, num_pixels).T.reshape(-1)


#
# TODO: Load up your face_labels dataset. It only has a single column, and
# you're only interested in that single column. You will have to slice the 
# column out so that you have access to it as a "Series" rather than as a
# "Dataframe". Use an appropriate indexer to take care of that. Also print
# out the labels and compare to the face_labels.csv file to ensure you
# loaded it correctly
#
face_label = pd.read_csv('/Users/ammarbahman/desktop/dat210x/Module5/Datasets/face_labels.csv', name='label)
y = face_label['label']

if Test_PCA:
  # INFO: PCA is used *before* KNeighbors to simplify your high dimensionality
  # image samples down to just 2 principal components! A lot of information
  # (variance) is lost during the process, as I'm sure you can imagine. But
  # you have to drop the dimension down to two, otherwise you wouldn't be able
  # to visualize a 2D decision surface / boundary. In the wild, you'd probably
  # leave in a lot more dimensions, but wouldn't need to plot the boundary;
  # simply checking the results would suffice.
  #

  #
  # TODO: Implement PCA here. Fit and transform your data. Make sure you do not
  # replace your original dataset and instead, store the results in a new
  # variable (e.g. "X" instead of df)
  #
  from sklearn.decomposition import PCA
  pca = PCA(n_components=2)
  pca.fit(df)
  X = pca.transform(df)

else:
  # INFO: Isomap is used *before* KNeighbors to simplify your high dimensionality
  # image samples down to just 2 components! A lot of information has been is
  # lost during the process, as I'm sure you can imagine. But if you have
  # non-linear data that can be represented on a 2D manifold, you probably will
  # be left with a far superior dataset to use for classification. Plus by
  # having the images in 2D space, you can plot them as well as visualize a 2D
  # decision surface / boundary. In the wild, you'd probably leave in a lot
  # more dimensions, but wouldn't need to plot the boundary; simply checking
  # the results would suffice.
  #

  #
  # TODO: Implement Isomap here. Fit and transform your data. Make sure you do not
  # replace your original dataset and instead, store the results in a new
  # variable (e.g. "X" instead of df)
  #
  from sklearn import manifold
  iso = manifold.Isomap(n_neighbors=5, n_components=2)
  iso.fit(df)
  X = iso.transform(df)


#
# TODO: Do train_test_split. Use the same code as on the EdX platform in the
# reading material, but set the random_state=7 for reproduceability, and play
# around with the test_size from 0.10 - 0.20 (10-20%). Your labels are actually
# passed in as a series (instead of as an NDArray) so that you can access
# their underlying indices later on. This is necessary so you can find your samples
# in the original dataframe, which you will use to plot your testing data as images
# rather than as points:
#

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=7) #X is the data and y is the label. I have to add a 0 in the beginning of face_label.csv becasue python took it as as aheading for the column


#
# TODO: Implement KNeighborsClassifier here. You can use any K value from 1
# through 20, so play around with it and attempt to get good accuracy.
# This is the heart of this assignment: Looking at the 2D points that
# represent your images, along with a list of "answers" or correct class
# labels that those 2d representations should be.
#
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3) #n_neighbors is KNeighbors values
model.fit(X_train, y_train)
#print model.predict([[1.1]])
#print model.predict_proba([[0.9]])


# NOTE: K-NEIGHBORS DOES NOT CARE WHAT THE ANSWERS SHOULD BE! In fact, it
# just tosses that information away. All KNeighbors cares about storing is
# your training data (data_train) so that later on when you attempt to
# predict or score samples, it can derive a class for them based on the
# labeling of the sample's near neighbors.
#
# TODO: Calculate + Print the accuracy of the testing set (data_test and
# label_test).
#
print model.score(X_test,y_test)



# Chart the combined decision boundary, the training data as 2D plots, and
# the testing data as small images so we can visually validate performance.
data_train, label_train, data_test, label_test = X_train, y_train, X_test, y_test #match out X, y to data and test
Plot2DBoundary(data_train, label_train, data_test, label_test)


