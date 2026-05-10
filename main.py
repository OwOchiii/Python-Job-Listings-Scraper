import logging
from scraper import scrape_jobs
from pipeline import process_and_cluster, plot_clusters

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    logging.info("--- Starting Fake Jobs Pipeline ---")
    
    # 1. Scrape
    scrape_jobs("jobs.csv")
    
    # 2. Process & Cluster
    df, X = process_and_cluster("jobs.csv", n_clusters=5)
    
    # 3. Visualize
    if df is not None:
        plot_clusters(df, X)
        logging.info("--- Pipeline Completed Successfully ---")
        
        # Simple Data Analysis Report Printout
        print("\n\n=== OVERALL DATA ANALYSIS REPORT ===")
        print(f"Total Jobs Parsed: {len(df)}")
        print("\nDistribution across Clusters:")
        print(df['Cluster'].value_counts().to_string())
        print("\nSample Data clustered as '0':")
        print(df[df['Cluster'] == 0][['Title', 'Location']].head(3).to_string(index=False))
        
if __name__ == "__main__":
    run()

