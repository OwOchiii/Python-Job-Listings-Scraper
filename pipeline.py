import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_and_cluster(input_csv="jobs.csv", n_clusters=5):
    if not os.path.exists(input_csv):
        logging.error(f"File {input_csv} not found.")
        return None, None

    logging.info(f"Loading data from {input_csv}")
    df = pd.read_csv(input_csv)
    
    # Deduplicate data to handle repeated scraping runs
    initial_len = len(df)
    df.drop_duplicates(inplace=True)
    if len(df) < initial_len:
        logging.info(f"Dropped {initial_len - len(df)} duplicate job entries.")
        
    if df.empty:
        logging.warning("Dataset is empty after deduplication.")
        return None, None
    
    # Combine title and location for a richer feature
    df['combined_feature'] = df['Title'] + " " + df['Location']
    
    logging.info("Vectorizing text data...")
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['combined_feature'])
    
    logging.info(f"Performing K-Means clustering with {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X)
    
    logging.info("Clustering complete.")
    return df, X

def plot_clusters(df, X):
    if df is None or X is None:
        logging.error("No data to plot.")
        return

    logging.info("Reducing dimensions for visualization...")
    pca = PCA(n_components=2, random_state=42)
    reduced_features = pca.fit_transform(X.toarray())
    
    df['PCA1'] = reduced_features[:, 0]
    df['PCA2'] = reduced_features[:, 1]
    
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(df['PCA1'], df['PCA2'], c=df['Cluster'], cmap='viridis', s=50, alpha=0.7)
    
    # Add legend
    legend1 = plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.gca().add_artist(legend1)
    
    plt.title("Job Postings Inter-Cluster PCA Visualization")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    
    output_img = "cluster_plot.png"
    plt.savefig(output_img)
    logging.info(f"Plot saved as {output_img}")
    plt.show()

if __name__ == "__main__":
    df, X = process_and_cluster()
    if df is not None:
        plot_clusters(df, X)
