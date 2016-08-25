import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("/Users/ammarbahman/desktop/dat210x/students.data", index_col=0)

pca = PCA(n_components=2)
print pca.fit(df)
#PCA(copy=True, n_components=2, whiten=False)

T = pca.transform(df)

print df.shape
#(430, 6) # 430 Student survey responses, 6 questions..

print T.shape
#(430, 2) # 430 Student survey responses, 2 principal components..