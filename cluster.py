import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("/Users/ammarbahman/desktop/dat210x/students.data", index_col=0)

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

