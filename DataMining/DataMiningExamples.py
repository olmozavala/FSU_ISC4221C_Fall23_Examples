# %%
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# %% Sample data
data = np.array([
    [1, 1], [1.2, 1.1], 
    [2, 1], [2.1, 1.1],
    
    [1, 3], [1.1, 3.2], 
    [2, 3], [2.1, 3.1],
    
    [5, 6], [5.1, 1.9],
    
    [7, 7], [7.1, 7.2],
    [8, 7], [8.1, 7.1]
])

# data = np.array([
#     [1, 1], [1.5, 2], [2, 3], [2.5, 4], [3, 5],
#     [3.5, 1], [4, 2], [4.5, 3], [5, 4], [5.5, 5],
#     [10, 10], [10.1, 10.2], [10.2, 9.9]
# ])


plt.figure(figsize=(4, 4))
plt.scatter(data[:, 0], data[:, 1])
for i, d in enumerate(data):
    plt.annotate(str(i), (d[0], d[1]))
plt.title('Data Points')
plt.show()

# %% Perform single linkage hierarchical clustering
Z_single = linkage(data, method='single', metric='euclidean')

# Plot dendrogram
plt.figure(figsize=(15, 5))
dendrogram(Z_single, labels=[str(i) for i, d in enumerate(data)]) # Angle the labels
# print(Z_single)
plt.title('Single Linkage Hierarchical Clustering Dendrogram')
plt.show()
# %%

# Euclidean distance between points 0 and 1
print(f'Distance between 0 and 1 {np.linalg.norm(data[6] - data[7]):0.4f}')

# %% Compute and plot complete linkage
Z_complete = linkage(data, method='complete', metric='euclidean')

# Plot both dendograms for complete and single linkage
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
dendrogram(Z_single, labels=[str(i) for i, d in enumerate(data)], ax=axs[0])
axs[0].set_title('Single Linkage Hierarchical Clustering Dendrogram')
dendrogram(Z_complete, labels=[str(i) for i, d in enumerate(data)], ax=axs[1])
axs[1].set_title('Complete Linkage Hierarchical Clustering Dendrogram')
plt.show()







# %% ----------------------------------------------------- k-means -----------------------


# %%
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.80, random_state=0)

# Plot the data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Input Data")
plt.show()

# %%
k_n = [2, 3, 4, 5, 6, 7, 8, 9, 10]
k_var = np.zeros(len(k_n))
for i, k in enumerate(k_n):
    # Apply k-means clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    # Compute the variance explained by the clustering
    k_var[i] = kmeans.score(X)
    print(f'Variance explained by {k} clusters: {k_var[i]:0.4f}')

    # Plot the results
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    # Plot the centroids
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
    plt.title("K-Means Clustering")
    plt.show()

# Plot the variance with respect to the number of clusters
plt.plot(k_n, k_var)
plt.xlabel('Number of clusters')
plt.ylabel('Variance explained')
plt.title('Variance explained by k-means clustering')
plt.show()

# %%
