# scraper.py

import requests
from bs4 import BeautifulSoup
import json
import time
from config import KEYWORDS, LOCATION, INDEED_BASE_URL, HEADERS

JOB_STORAGE_FILE = "job_data.json"


def load_previous_jobs():
    try:
        with open(JOB_STORAGE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_new_jobs(jobs):
    with open(JOB_STORAGE_FILE, "w") as file:
        json.dump(jobs, file, indent=4)


def fetch_jobs():
    found_jobs = []
    seen_jobs = load_previous_jobs()

    for keyword in KEYWORDS:
        query = keyword.replace(" ", "+")
        url = f"{INDEED_BASE_URL}?q={query}&l={LOCATION}"

        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.find_all("a", attrs={"data-hide-spinner": "true"})

        for job in job_cards:
            title_elem = job.find("span")
            company_elem = job.find_parent().find("span", class_="companyName")
            location_elem = job.find_parent().find("div", class_="companyLocation")

            if not title_elem or not company_elem or not location_elem:
                continue

            job_info = {
                "title": title_elem.text.strip(),
                "company": company_elem.text.strip(),
                "location": location_elem.text.strip(),
                "link": f"https://www.indeed.com{job['href']}"
            }

            if job_info not in seen_jobs:
                found_jobs.append(job_info)
                seen_jobs.append(job_info)

        time.sleep(1)  # Be polite to Indeed’s server

    if found_jobs:
        save_new_jobs(seen_jobs)

    return found_jobs
