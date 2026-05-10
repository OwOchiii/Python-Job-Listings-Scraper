# Fake Job Listings: Scraper & Analysis

This project demonstrates a full data pipeline for scraping job listings from a mock website, processing the text data, and using unsupervised machine learning to identify job clusters.

## Project Overview

The primary goal is to extract job data (Title, Company, Location) from the [RealPython Fake Jobs](https://realpython.github.io/fake-jobs/) website and group similar jobs together based on their descriptions and locations.

The pipeline consists of:
1.  **Scraper (`scraper.py`):** Fetches HTML using `requests` and parses it with `BeautifulSoup` to extract job listings into a `jobs.csv` file.
2.  **Pipeline (`pipeline.py`):** Cleans the data, combines job titles and locations, and uses `scikit-learn` to perform TF-IDF vectorization and K-Means clustering.
3.  **Visualization (`main.py` & `eda_workspace.ipynb`):** The results are visualized using `matplotlib` after reducing dimensions with PCA, and a brief report is generated.

---

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd python-job-listings-scraper
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

There are two ways to run this project:

### 1. Production Script (`main.py`)
This script runs the entire pipeline from start to finish: scraping, clustering, and generating a plot (`cluster_plot.png`).

To run it, execute the following command in your terminal:
```bash
python main.py
```

### 2. Interactive EDA (`eda_workspace.ipynb`)
For a more hands-on, exploratory approach, use the Jupyter Notebook.

1.  Start the Jupyter server:
    ```bash
    jupyter notebook
    ```
2.  In the browser window that opens, click on `eda_workspace.ipynb`.
3.  Run the cells one by one to see the data loading, cluster distribution, and sample data from each group.

---

## Data Analysis Report

### Methodology
After scraping 100 job listings, we combined the **Job Title** and **Location** into a single text feature. This combined feature was then converted into a numerical format using TF-IDF vectorization, which helps the model understand the relative importance of different words. Finally, K-Means clustering was applied to group the jobs into 5 distinct clusters.

### Results & Interpretation
The clustering algorithm grouped the 100 jobs as follows:

*   **Cluster 3:** 30 jobs
*   **Cluster 4:** 30 jobs
*   **Cluster 0:** 24 jobs
*   **Cluster 2:** 12 jobs
*   **Cluster 1:** 4 jobs

By inspecting the jobs within each cluster, we can infer what defines them:

*   **Cluster 0 (Sample: *Fitness centre manager, Medical technical officer*)**: This cluster appears to group **service-oriented and hands-on technical roles**. The locations are varied, suggesting the job *title* was the primary factor for grouping.

*   **Cluster 2 (12 jobs)**: This cluster likely represents a specific subset of specialized roles or a particular geographic region that stands apart from the main groupings but isn't as rare as Cluster 1.

*   **Clusters 3 & 4**: These are the largest groups and likely represent the most common job types in the dataset, such as **"Engineer"** or **"Analyst"**. The model successfully separated them, which could be due to location differences (e.g., "East Coast Engineers" vs. "West Coast Engineers") or specializations (e.g., "Data Engineer" vs. "Systems Engineer").

*   **Cluster 1 (4 jobs)**: This is the smallest and most unique cluster. These jobs likely have very distinct titles or locations that are rare in the dataset, making them stand out as a separate group. For example, a highly specialized role like "Astronomer" located in a unique city would likely be isolated here.

### Conclusion
The model successfully identified distinct groupings within the job data, primarily driven by job function and, to a lesser extent, location. This demonstrates that even with a simple dataset, unsupervised learning can uncover meaningful patterns that would be difficult to spot manually.

Project webpage: https://roadmap.sh/projects/job-listings-scraper
