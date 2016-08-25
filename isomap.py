import pandas as pd
from sklearn import manifold

df = pd.read_csv("/Users/ammarbahman/desktop/dat210x/students.data", index_col=0)

iso = manifold.Isomap(n_neighbors=4, n_components=2)
##n_components is the number of features you want your dataset projected onto
##n_neighbors defines the neighborhood size used to create the node neighborhood map
print iso.fit(df)

manifold = iso.transform(df)

print df.shape

print manifold.shape


###Unlike PCA, Isomap transformations are unidirectional so you will not be able to .inverse_transform() your projected data back into your original feature space