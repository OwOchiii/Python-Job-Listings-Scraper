import requests
from bs4 import BeautifulSoup
import csv
import logging
import os

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs(output_csv="jobs.csv"):
    logging.info(f"Starting to fetch data from {URL}")
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")

    jobs = []
    for job_elem in job_elements:
        title_element = job_elem.find("h2", class_="title")
        company_element = job_elem.find("h3", class_="company")
        location_element = job_elem.find("p", class_="location")
        created_date_element = job_elem.find("time")

        # Basic cleanup
        title = title_element.text.strip() if title_element else "N/A"
        company = company_element.text.strip() if company_element else "N/A"
        location = location_element.text.strip() if location_element else "N/A"
        created_date = created_date_element.text.strip() if created_date_element else "N/A"

        jobs.append([title, company, location, created_date])

    logging.info(f"Successfully scraped {len(jobs)} jobs.")

    file_exists = os.path.exists(output_csv)
    
    try:
        with open(output_csv, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Title", "Company", "Location","Created Date"])
            writer.writerows(jobs)
        logging.info(f"Successfully saved data to {output_csv}")
    except IOError as e:
        logging.error(f"Error writing to file: {e}")

if __name__ == "__main__":
    scrape_jobs()
